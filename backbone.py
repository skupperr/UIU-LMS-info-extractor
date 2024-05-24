from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
from multiprocessing import Process, Queue
import excel_file
import subprocess

person_profile_list = []
q1 = Queue()
q2 = Queue()


def get_chrome_install_location(browser):

    command = f'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\{browser}.exe'
    try:
        # Run the reg query command
        result = subprocess.run(
            ['reg', 'query', command, '/ve'],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        
        # Parse the output to find the line that contains the default value
        for line in output.splitlines():
            if '(Default)' in line:
                # The path will be after the last space in the line
                install_location = line.split('    ')[-1].strip()
                
                path = install_location
                x = path.split('\\')
                path = "\\\\".join(x)
                print(path)
                return path
                
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False



def check_email(email):

    pattern = r'@\w+\.uiu\.ac\.bd'
    check = re.search(pattern,email)
    if check:
        return True
    else:
        return False
    

def check_id(id):

    # try catch is for if variable id contains any alphabets
    try:
        id = int(id)
    except:
        return False
    
    if(id >= 0 and id <= 10000000000):
        return True
    else:
        return False


def person_profile(username, password, link):
    
    global file_name

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless= True, slow_mo=50, executable_path= chrome_path)
        except:
            browser = p.chromium.launch(headless= True, slow_mo=50, executable_path= edge_path)

        page = browser.new_page()
        page.goto("https://lms.uiu.ac.bd/login/index.php")
        page.fill('input#username', username)
        page.fill('input#password', password)
        page.click('button#loginbtn')
        
        # Whether login was invalid or not
        element = page.query_selector(f".{'loginerrors'}")
        if element:
            return element.is_visible()

        try:
            page.goto(f"{link}&perpage=5000")
            #page.wait_for_selector("div[data-grid-item=true]")
            page.wait_for_load_state('networkidle')
            html = page.inner_html('#page-wrapper')
            soup = BeautifulSoup(html, 'html.parser')

            # Whether link was valid or not
            h2_text = soup.select('h2')[0].get_text()
            if(h2_text != "Participants"):
                raise Exception()
        except Exception as e:
            print(e)
            return 5

        # Capturing the course code and name to name the excel file
        file_name = (soup.select(".page-header-headings h1")[0]).get_text()
        file_name = file_name.split(":")
        file_name = file_name[0]

        # Removing unsupported file name characters
        file_name = file_name.replace('\\', '')
        file_name = file_name.replace('/', '')
        file_name = file_name.replace(':', '')
        file_name = file_name.replace('*', '')
        file_name = file_name.replace('?', '')
        file_name = file_name.replace('<', '')
        file_name = file_name.replace('"', '')
        file_name = file_name.replace('>', '')
        file_name = file_name.replace('|', '')

        # the number of participants in a course
        name = soup.select('p')[0].getText()
        number_of_participants = int((re.findall(r'\d+', name))[0])

        page.is_visible('div.no-overflow')

        i = 0
        while(i < number_of_participants):

            try:
                list = soup.select('.cell.c0')
                l = list[i]
                person_profile = l.find('a')['href']   # participant profile link

                roles = soup.select('.cell.c1')
                if((roles[i].get_text()) != "Student"):
                    i+=1
                    continue

                person_profile_list.append(person_profile)

                i+=1
            except:
                i+=1
        browser.close()
        

def task_divider(username, password, links):
    l = len(links)

    n1 = l//4
    n2 = n1 + l//4
    n3 = n2 + l//4

    a = Process(target= get_individual_info, args= (0, n1, username, password, person_profile_list, q1, chrome_path, edge_path))
    b = Process(target= get_individual_info, args= (n1, n2, username, password, person_profile_list, q1, chrome_path, edge_path))
    c = Process(target= get_individual_info, args= (n2, n3, username, password, person_profile_list, q2, chrome_path, edge_path))
    d = Process(target= get_individual_info, args= (n3, l, username, password, person_profile_list, q2, chrome_path, edge_path))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()



def get_individual_info(start, end, username, password, lists, queue, chrome_path, edge_path):


    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless= True, slow_mo=50, executable_path= chrome_path)
        except:
            browser = p.chromium.launch(headless= True, slow_mo=50, executable_path= edge_path)
           

        page = browser.new_page()
        link = "https://lms.uiu.ac.bd/login/index.php"
        page.goto(link)
        page.fill('input#username', username)
        page.fill('input#password', password)
        page.click('button#loginbtn')

        for i in range(start, end):
            try:
                page.goto(lists[i])
                #page.wait_for_selector("div[data-grid-item=true]")
                page.wait_for_load_state('networkidle')

                html = page.inner_html('#page-wrapper')
                soup = BeautifulSoup(html, 'html.parser')

                email_class = soup.select('.node_category')
                email = ((email_class[0]).find('a')).text.strip()

                name_class = soup.select('.page-header-headings h2')
                s = name_class[0].get_text()
                l = s.split()
                id = l[0]
                if(check_id(id)):
                    l.pop(0)
                else:
                    id = "N/A"
                name = " ".join(l)
                
                if check_email(email):
                    di = {
                        "name":name,
                        "id":id,
                        "email":email,
                    }
                    
                    queue.put(di)
            except Exception as e:
                print(e)


    
def main(username, password, link):

    global chrome_path
    global edge_path

    chrome_path = get_chrome_install_location('chrome')
    edge_path = get_chrome_install_location('msedge')

    if(chrome_path == False and edge_path == False):
        return 10

    a = person_profile(username, password, link)
    
    if(a == True): 
        return False
    
    elif(a == 5):
        return 5

    else:
        task_divider(username, password, person_profile_list)
        excel_file.creating_excel_file(file_name, q1, q2)
        return True

