from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import webbrowser
import backbone
import threading
from multiprocessing import freeze_support

freeze_support()

def callback(url):
   webbrowser.open_new_tab(url)

def show():
    hide_button = Button(body_frame, image= hide_image, relief=FLAT, activebackground='white',  background='white', command= hide)
    hide_button.grid(row = 2, column= 3, padx= 10)
    password_entry.config(show= '')

def hide():
    hide_button = Button(body_frame, image= show_image, relief=FLAT, activebackground='white',  background='white', command= show)
    hide_button.grid(row = 2, column= 3, padx= 10)
    password_entry.config(show= '*')

def about():
    global img
    global frame1
    messagebox= Toplevel(bg="#211F1E")
    messagebox.title("About")
    messagebox.geometry("400x180")
    messagebox.resizable(False, False)


    frame1= Frame(messagebox, bg="#211F1E")
    frame1.pack()

    l = Label(frame1, text= "Developed by:", font=("Arial", 12), bg="#211F1E", fg= "White")
    l.grid(row= 0, column= 0)
    img= ImageTk.PhotoImage(file = 'D:\\Python\\Web Scrapping\\LMS email extractor\\abc.png')
    img_label= Label(frame1, image= img, bg="#211F1E")
    img_label.grid(row=1, column= 0)
    name = Label(frame1, text= "ASIF U. AHMED", font= ("Helvetica", 10), bg="#211F1E", fg= "White").grid(row= 3, column=0)
    l = Label(frame1, text= "hhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjjjjjjjjjj", font=("Arial", 12),bg="#211F1E", fg='#211F1E').grid(row = 1, column=1)

    version = Label(frame1, text= "UIU LMS INFO EXTRACTOR", bg="#211F1E",fg="white", font= ("Helvetica", 10)).place(x = 144, y = 50)
    version = Label(frame1, text= "Version : 1.0", font= ("Helvetica", 10), bg="#211F1E", fg= "white").place(x = 144, y = 70)

    l = Label(frame1, text= "Contact Info: ", bg="#211F1E", fg= "White").place(x = 144, y = 147)

    ig_link = Label(frame1, image=ig ,font=('Helveticabold', 15), bg="#211F1E", fg="blue", cursor="hand2")
    ig_link.place(x= 220, y = 147)
    ig_link.bind("<Button-1>", lambda e: callback("https://www.instagram.com/skupperr/"))

    fb_link = Label(frame1, image=fb ,font=('Helveticabold', 15), bg="#211F1E", fg="blue", cursor="hand2")
    fb_link.place(x= 245, y = 147)
    fb_link.bind("<Button-1>", lambda e: callback("https://www.facebook.com/skupperr/"))

    ld_link = Label(frame1, image=ld ,font=('Helveticabold', 15), bg="#211F1E", fg="blue", cursor="hand2")
    ld_link.place(x= 270, y = 147)
    ld_link.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/asifuahmed/"))

    git_link = Label(frame1, image=git ,font=('Helveticabold', 15), bg="#211F1E", fg="blue", cursor="hand2")
    git_link.place(x= 295, y = 147)
    git_link.bind("<Button-1>", lambda e: callback("https://github.com/skupperr"))

def thread_executer():

    username = username_entry.get()
    password = password_entry.get()
    link = link_entry.get()

    username_entry.config(state= "disabled")
    password_entry.config(state= "disabled")
    link_entry.config(state= "disabled")
    proceed_button.config(state= "disabled")

    process_label.config(text= "Please wait while your request is being processed.")

    x = threading.Thread(target= execute, args= (username, password, link, ), daemon= True)
    x.start()


def execute(username, password, link):

    a = backbone.main(username, password, link)
    if(a == False):
        messagebox.showerror("Error",  "Invalid username or password.")
        process_label.config(text='')
    elif(a == 5):
        messagebox.showerror("Error",  "Invalid link.")
        process_label.config(text='')
    else:
        messagebox.showinfo("Success", "Informations retrieved successfully.")
        process_label.config(text='')

    username_entry.config(state= "normal")
    username_entry.delete(0, END)
    password_entry.config(state= "normal")
    password_entry.delete(0, END)
    link_entry.config(state= "normal")
    link_entry.delete(0, END)
    proceed_button.config(state= "normal")

def home():
    forget_frame()
    global password_entry
    global username_entry
    global link_entry
    global proceed_button
    global process_label

    body_frame.pack(fill='y', expand=1)

    username_label = Label(body_frame, text="Username: ", font=("Arial", 15), bg= 'white')
    username_label.grid(row=1, column = 1, pady=10)

    username_entry = Entry(body_frame, font=("helvetica", 15), highlightbackground="Silver", highlightcolor="Silver", highlightthickness=1)
    username_entry.grid(row= 1, column= 2, pady=10)

    password_label = Label(body_frame, text="Password: ", font=("Arial", 15), bg = "white")
    password_label.grid(row=2, column = 1, pady=10)

    password_entry = Entry(body_frame, font=("helvetica", 15), highlightbackground="Silver", highlightcolor="Silver", highlightthickness=1, show="*")
    password_entry.grid(row= 2, column= 2, pady=10)

    show_button = Button(body_frame, image= show_image, relief=FLAT, activebackground='white',  background='white', command= show)
    show_button.grid(row = 2, column= 3, padx= 10)

    link_label = Label(body_frame, text= "Link: ", font=("helvetica", 11), bg='white')
    link_label.grid(row= 3, column= 0, pady= 20)

    link_entry = Entry(body_frame, font=("helvetica", 10), highlightbackground="Silver", highlightcolor="Silver", highlightthickness=1, width= 49)
    link_entry.place(x = 50, y = 119)

    
    proceed_button = Button(body_frame, text= "Proceed", command= thread_executer)
    proceed_button.place(x = 190, y = 160)

    process_label = Label(body_frame, text="", font= ("Helvetica", 12), bg= 'white')
    process_label.place(x = 30, y = 200)


def forget_frame():
    try:
        body_frame.pack_forget()
        tutorial_frame.pack_forget()
    except:
        pass

def tutorial():
    global tutorial_frame
    forget_frame()

    tutorial_frame = Frame(window, bg = 'white')
    tutorial_frame.pack(fill= 'y', expand=1)

    text = '''1. Launch the browser of your choice.
2. Open the LMS site and log in.
3. Navigate to the Participants page of the course from which 
    you need to retrieve participant data.
4. Copy the link in the address bar.
5. The URL should have this format: 
    https://lms.uiu.ac.bd/user/index.php?id=****
'''
    text_label = Label(tutorial_frame, text= text, font=("Helvetica", 12), justify= LEFT).pack(side= RIGHT)


def gui():
    global show_image, hide_image, body_frame, ig, fb, ld, git, window, gif_image, loading_frame

    window = Tk()
    window.geometry("480x250")
    window.resizable(False,False)
    window.configure(bg="white")
    window.title("LMS Info Extractor")

    show_image = ImageTk.PhotoImage(file = 'D:\\Python\\Web Scrapping\\LMS email extractor\\show.png')
    hide_image = ImageTk.PhotoImage(file = 'D:\\Python\\Web Scrapping\\LMS email extractor\\hide.png')
    ig = ImageTk.PhotoImage(file ="D:\\Python\\Web Scrapping\\LMS email extractor\\instagram.png")
    fb = ImageTk.PhotoImage(file ="D:\\Python\\Web Scrapping\\LMS email extractor\\facebook.png")
    ld = ImageTk.PhotoImage(file ="D:\\Python\\Web Scrapping\\LMS email extractor\\linkedin.png")
    git = ImageTk.PhotoImage(file ="D:\\Python\\Web Scrapping\\LMS email extractor\\github.png")
    show_image = ImageTk.PhotoImage(file = 'D:\\Python\\Web Scrapping\\LMS email extractor\\show.png')
    hide_image = ImageTk.PhotoImage(file = 'D:\\Python\\Web Scrapping\\LMS email extractor\\hide.png')

    gif_image = "D:\\Python\\Web Scrapping\\LMS email extractor\\giff.gif"
    

    myMenu=Menu(window)
    window.config(menu= myMenu)

    body_frame = Frame(window, bg="white")
    loading_frame = Frame(window, bg = 'red')
    home()    

    help_menu=Menu(myMenu, tearoff= False)
    myMenu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Home", command= home)
    help_menu.add_command(label="Tutorial", command= tutorial)
    help_menu.add_separator()
    help_menu.add_command(label="About", command= about)

    window.mainloop()


if __name__ == '__main__':
    gui()


