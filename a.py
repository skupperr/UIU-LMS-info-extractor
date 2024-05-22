from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

def check_email(email):
    #pattern = r'@\w+\.com'
    pattern = r'@\w+\.uiu\.ac\.bd'
    check = re.search(pattern,email)
    if check:
        return True
    else:
        return False

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False, slow_mo= 1000)
    page = browser.new_page()
    link = "https://lms.uiu.ac.bd/login/index.php"
    page.goto(link)
    page.fill('input#username', '0112230002')
    page.fill('input#password', 'AhmedCSEUIU7869')
    page.click('button#loginbtn')

    link = "https://lms.uiu.ac.bd/user/index.php?id=2919"
    
    page.goto(f"{link}&perpage=5000")
    html = page.inner_html('#page-wrapper')

    soup = BeautifulSoup(html, 'html.parser')
    h2 = soup.select('h2')[0].get_text()

    try:
        a = soup.select("alert alert-danger")[0].get_text()
        print(a)
        if(a == "Invalid login, please try again"):
            print("Invalid")
    except:
        pass
    
    name = soup.select('p')[0].getText()
    number_of_participants = int((re.findall(r'\d+', name))[0])
    
    print(number_of_participants)

    page.is_visible('div.no-overflow')

    i = 0
    # while(i < number_of_participants):

    #     try:
    #         list = soup.select('.cell.c0')
    #         l = list[i]
    #         person_profile = l.find('a')['href']

    #         roles = soup.select('.cell.c1')
    #         if((roles[i].get_text()) != "Student"):
    #             i+=1
    #             continue

    #         page.goto(person_profile)
    #         html = page.inner_html('#page-wrapper')
    #         soup = BeautifulSoup(html, 'html.parser')

    #         email_class = soup.select('.node_category')
    #         email = ((email_class[0]).find('a')).text.strip()

    #         if check_email(email):
    #             print(email)

    #         i+=1
    #     except:
    #         i+=1
    #         pass

    #     page.goto(f"{link}&perpage=5000")
    #     page.is_visible('div.no-overflow')
    #     html = page.inner_html('#page-wrapper')
    #     soup = BeautifulSoup(html, 'html.parser')
    