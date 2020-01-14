import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import Listbox
import pygame


# ====================================Register==========================================
def user_Register(disability):
    root = tk.Toplevel()
    root.title("AccessWord: Register User")
    width = 550
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()
    PASSWORD2 = StringVar()
    AGE = StringVar()
    EMAIL = StringVar()
    DISABILITY = StringVar()

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `User_Blind` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT , age TEXT, email TEXT)")
        cursor.execute(
            "SELECT * FROM `User_Blind` WHERE `username` = 'admin' AND `password` = 'admin' AND `age` = 'admin' AND `email` = 'admin'")

    def Register(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "" or AGE.get() == "" or EMAIL.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            if (disability == 'visually impaired'):
                cursor.execute("SELECT `username` FROM `User_Blind`")
                record = cursor.fetchall()
                found = False
                for row in record:
                    if USERNAME.get() == row[0]:
                        lbl_text.config(text="User Exsiests!!!", fg="red")
                        USERNAME.set("")
                        PASSWORD.set("")
                        PASSWORD2.set("")
                        found = True
                if found == False:
                    cursor.execute("INSERT INTO `User_Blind` (username, password, age, email) VALUES (?,?,?,?)",
                                   (USERNAME.get(), PASSWORD.get(), AGE.get(), EMAIL.get()))
                    conn.commit()
                    HomeWindow()

            elif (disability == 'Hearing impaired'):
                cursor.execute("SELECT `username` FROM `User_Deaf`")
                record = cursor.fetchall()
                found = False
                for row in record:
                    if USERNAME.get() == row[0]:
                        lbl_text.config(text="User Exsiests!!!", fg="red")
                        USERNAME.set("")
                        PASSWORD.set("")
                        PASSWORD2.set("")
                        found = True
                if found == False:
                    cursor.execute("INSERT INTO `User_Deaf` (username, password, age, email) VALUES (?,?,?,?)",
                                   (USERNAME.get(), PASSWORD.get(), AGE.get(), EMAIL.get()))
                    conn.commit()
                    HomeWindow()

        cursor.close()
        conn.close()

    def HomeWindow():
        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("AccessWord: Register User")
        width = 400
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Register!", font=('times new roman', 20)).pack()
        btn_back = Button(Home, text='OK', command=CloseRegister).pack(pady=20, fill=X)

    def CloseRegister():
        Home.destroy()
        keyboard()  # Change To User_Blind Frame!!!

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="AccessWord: Register User", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_password2 = Label(Form, text="Enter Password again:", font=('arial', 14), bd=15)
    lbl_password2.grid(row=2, sticky="e")
    lbl_age = Label(Form, text="Age:", font=('arial', 14), bd=15)
    lbl_age.grid(row=3, sticky="e")
    lbl_email = Label(Form, text="Email:", font=('arial', 14), bd=15)
    lbl_email.grid(row=4, sticky="e")
    lbl_disability = Label(Form, text="Disability:", font=('arial', 14), bd=15)
    lbl_disability.grid(row=5, sticky="e")
    lbl_disabilityshow = Label(Form, text=disability, font=('arial', 14), bd=15)
    lbl_disabilityshow.grid(row=5, column=1)
    lbl_text = Label(Form)
    lbl_text.grid(row=6, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    var1 = BooleanVar()

    def showpass():
        if (var1.get() == 0):
            password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
            password.grid(row=1, column=1)
            password2 = Entry(Form, textvariable=PASSWORD2, show="*", font=(14))
            password2.grid(row=2, column=1)
        else:
            password = Entry(Form, textvariable=PASSWORD, font=(14))
            password.grid(row=1, column=1)
            password2 = Entry(Form, textvariable=PASSWORD2, font=(14))
            password2.grid(row=2, column=1)

    Checkbutton(Form, text="show password", variable=var1, command=showpass).grid(row=1, column=3)
    showpass()
    age = Entry(Form, textvariable=AGE, font=(14))
    age.grid(row=3, column=1)
    email = Entry(Form, textvariable=EMAIL, font=(14))
    email.grid(row=4, column=1)
    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Register", width=45, command=Register)
    btn_login.grid(pady=0, row=8, columnspan=2)
    btn_login.bind('<Return>', Register)
    # btn_register = Button(Form, text="Register", width=20, command=Register_Win)
    # btn_register.grid(pady=10, row=4, columnspan=2)
    # btn_register.bind('<Return>', Login)


# ====================================Register==========================================
# ========================user_login_blind========================
def user_login_blind():
    root = tk.Toplevel()
    root.title("AccessWord: user Login")
    width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `User_Blind` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `User_Blind` WHERE `username` = 'admin' AND `password` = 'admin'")

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `User_Blind` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    def HomeWindow():
        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("AccessWord: User Login")
        width = 400
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
        btn_back = Button(Home, text='OK', command=CloseLogin).pack(pady=20, fill=X)

    def CloseLogin():
        Home.destroy()
        keyboard()  # Change To User_Blind Frame!!!

    def user_Register_blind():
        root.destroy()
        user_Register('visually impaired')

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="AccessWord: User Login", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=0, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)
    btn_register = Button(Form, text="Register", width=20, command=user_Register_blind)
    btn_register.grid(pady=10, row=4, columnspan=2)
    btn_register.bind('<Return>', Login)


# ========================user_login_blind========================


# ========================user_login_deaf========================
def user_login_deaf():
    root = tk.Toplevel()
    root.title("AccessWord: user Login")
    width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `User_Deaf` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `User_Deaf` WHERE `username` = 'admin' AND `password` = 'admin'")
        # if cursor.fetchone() is None:
        # cursor.execute("INSERT INTO `User_Deaf` (username, password) VALUES('admin', 'admin')")
        # conn.commit()

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `User_Deaf` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    def HomeWindow():
        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("AccessWord: User Login")
        width = 400
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
        btn_back = Button(Home, text='OK', command=CloseLogin).pack(pady=20, fill=X)

    def CloseLogin():
        Home.destroy()
        keyboard()  # Change To User_Blind Frame!!!

    def user_Register_hearing():
        root.destroy()
        user_Register('Hearing impaired')

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="AccessWord: User Login", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=0, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)
    btn_register = Button(Form, text="Register", width=20, command=Login)
    btn_register.grid(pady=10, row=4, columnspan=2)
    btn_register.bind('<Return>', Login)
    btn_register = Button(Form, text="Register", width=20, command=user_Register_hearing)
    btn_register.grid(pady=10, row=4, columnspan=2)
    btn_register.bind('<Return>', Login)


# ========================user_login_deaf========================

# ========================Admin_Login========================
def admin_login():
    root = tk.Toplevel()
    root.title("AccessWord: Admin Login")
    width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `Admin` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `Admin` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `Admin` (username, password) VALUES('admin', 'admin')")
            conn.commit()

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `Admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    def HomeWindow():
        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("Python: Simple Login Application")
        width = 400
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
        btn_back = Button(Home, text='OK', command=CloseLogin).pack(pady=20, fill=X)

    def CloseLogin():
        Home.destroy()
        Admin_Frame()

    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="AccessWord: Admin Login", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)


# ========================End of Admin_Login========================
# ========================Admin_Frame========================
def Admin_Frame():
    def Admin_Frame_Main():
        root = tk.Toplevel()
        #        HEAD
        root.title("AccessWord: Admin")
        width = 380
        height = 180
        # ================================================
        root.title("AccessWord: Admin Options")
        width = 380
        height = 200

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        # ------Buttons------
        button1 = Button(root, text="Show Users Of AccessWord", command=Show_users)
        button1.pack()
        button1.place(relx=0.5, rely=0.3, anchor=CENTER)
        button2 = Button(root, text="Show Reports", command=Show_reports)
        button2.pack()
        button2.place(relx=0.5, rely=0.5, anchor=CENTER)
        # ================ HEAD

        button3 = Button(root, text="Open KeyBoard", command=keyboard)
        button3.pack()
        button3.place(relx=0.5, rely=0.7, anchor=CENTER)
        button4 = Button(root, text="contact to developer", command=Show_contact)
        button4.pack()
        button4.place(relx=0.5, rely=0.9, anchor=CENTER)
        # ------Labels------
        lbl_title = Label(root, text="AccessWord: Admin Options", font=('arial', 15))
        lbl_title.pack(fill=X)

    def Show_users():
        root = tk.Toplevel()
        root.title("AccessWord: Users Of AccessWord")
        width = 750
        height = 580
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        # ===================== HEAD

        scrollbar = tk.Scrollbar(root, orient="vertical")
        listbox = tk.Listbox(root, font=('ariel', 10), width=90, height=20)
        listbox.pack(expand='yes', fill='both')
        listbox.place(relx=0.5, rely=0.5, anchor=CENTER)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.insert('end',
                       '{:20s}|{:20s}|{:10s}|{:40s}|{:10s}'.format(('UserName'), ('Password'), ('Age'), ('Email'),
                                                                   ('Phone')))

        def viewUsers(x):
            listbox.delete(0, 'end')
            listbox.insert('end',
                           '{:20s}|{:20s}|{:10s}|{:40s}|{:10s}'.format(('UserName'), ('Password'), ('Age'), ('Email'),
                                                                       ('Phone')))
            if (x == 'visually impaired'):
                conn = sqlite3.connect("AdminPassword.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM `User_Blind`")
                record = cur.fetchall()
                for row in record:
                    listbox.insert('end',
                                   '{:20s}|{:20s}|{:10s}|{:40s}|{:10s}'.format(row[1], row[2], row[3], row[4], row[5]))
            else:
                conn = sqlite3.connect("AdminPassword.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM `User_Deaf`")
                record = cur.fetchall()
                for row in record:
                    listbox.insert('end',
                                   '{:20s}|{:20s}|{:10s}|{:40s}|{:10s}'.format(row[1], row[2], row[3], row[4], row[5]))

        # ------Buttons------
        button1 = Button(root, text="Visually impaired", command=lambda: viewUsers('visually impaired'))
        button1.pack()
        button1.place(relx=0.3, rely=0.05, anchor=CENTER)
        button2 = Button(root, text="Hearing impaired", command=lambda: viewUsers('Hearing impaired'))
        button2.pack()
        button2.place(relx=0.6, rely=0.05, anchor=CENTER)

    def Show_reports():
        root = tk.Toplevel()
        root.title("AccessWord: Reports")
        width = 550
        height = 480
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

    # ================ HEAD

    def Show_contact():
        root = tk.Toplevel()
        root.title("AccessWord: Contact To Developer")
        width = 380
        height = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        # ---Frames---
        Top = Frame(root, bd=2, relief=RIDGE)
        Top.pack(side=TOP, fill=X)
        Form = Frame(root, height=200)
        Form.pack(side=TOP, pady=0)
        Form.place(relx=0.1, rely=0.2)
        # ---End Frames---
        lbl_title = Label(Top, text="Contact To Developer", font=('arial', 15))
        lbl_title.pack(fill=X)
        lbl_name = Label(Form, text="Name:", font=('arial', 12), bd=15)
        lbl_name.grid(row=0, column=0, sticky="e")
        lbl_email = Label(Form, text="Email:", font=('arial', 12), bd=15)
        lbl_email.grid(row=1, column=0, sticky="e")
        lbl_phone = Label(Form, text="Phone Number:", font=('arial', 12), bd=15)
        lbl_phone.grid(row=2, column=0, sticky="e")
        ###
        lbl_name_s = Label(Form, text="SCE", font=('arial', 12), bd=15)
        lbl_name_s.grid(row=0, column=1, sticky="e")
        lbl_email_s = Label(Form, text="Oshreav@ac.sce.ac.il", font=('arial', 12), bd=15)
        lbl_email_s.grid(row=1, column=1, sticky="e")
        lbl_phone_s = Label(Form, text="0504995388", font=('arial', 12), bd=15)
        lbl_phone_s.grid(row=2, column=1, sticky="e")

    Admin_Frame_Main()


# ========================End of Admin_Frame========================

def select(value):
    if value == "BACK":
        entry.delete(len(entry.get()) - 1, END)
        play(value)

    elif value == "SPACE":
        entry.insert(END, ' ')
        play(value)
    elif value == " Tab ":
        entry.insert(END, '    ')
        play(value)
    else:
        entry.insert(END, value)
        play(value)


def HosoPop(kb):
    varRow = 2
    varColumn = 0

    def OptionsKeyboard():
        kb = tk.Toplevel()
        kb.title("KeyBoard - Options")
        width = 600
        height = 600
        screen_width = kb.winfo_screenwidth()
        screen_height = kb.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        kb.geometry("%dx%d+%d+%d" % (width, height, x, y))
        kb.resizable(0, 0)

    for button in buttons:

        command = lambda x=button: select(x)

        if button == "Space":
            Button(kb, text=button, width=70, bg="#3c4987", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, command=lambda x=button: select(" ")).grid(row=5, column=0, columnspan=11)

        elif (button == "Options"):
            Button(kb, text=button, width=10, bg="#6D6D6D", fg="#0007AB",
                   activebackground="#000000", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, command=OptionsKeyboard).grid(row=2, column=16)
        else:
            Button(kb, text=button, width=5, bg="#3c4987", fg="#ffffff",
                   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=4,
                   pady=4, bd=2, command=command).grid(row=varRow, column=varColumn, )

        varColumn += 1
        if varColumn > 14 and varRow == 2:
            varColumn = 0
            varRow += 1
        if varColumn > 14 and varRow == 3:
            varColumn = 0
            varRow += 1


def keyboard():
    kb = Toplevel()
    kb.title("AccessWord")
    kb.resizable(0, 0)
    # kb.configure(bg='black')
    global entry
    entry = Entry(kb, width=128)
    entry.grid(rowspan=1, columnspan=15, ipadx=100, ipady=20)
    # entry.pack()
    HosoPop(kb)


buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
           'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
           'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', 'SHIFT', '1', '2', '3', '/',
           'Space', 'Options']


# outputing the sound to the keyboard
def play(buttons):
    pygame.init()
    sound1 = "sound\\" + buttons + ".ogg"
    pygame.mixer.music.load("sound\\" + buttons + ".ogg")
    pygame.mixer.music.play()



# Main Window #

root = Tk()
root.title("AccessWord")
l = Label(root, text="!שלום")
l.place(relx=0.45, rely=0.1)
l = Label(root, text=":אנא בחר את סוג המקלדת הרצויה")
l.place(relx=0.3, rely=0.25)
button1 = Button(root, text="Admin", command=admin_login)
button1.pack()
button1.place(relx=0.5, rely=0.6, anchor=CENTER)
button2 = Button(root, text="Hearing impaired", command=user_login_deaf)
button2.pack()
button2.place(relx=0.7, rely=0.6, anchor=CENTER)
button3 = Button(root, text="visually impaired", command=user_login_blind)
button3.pack()
button3.place(relx=0.3, rely=0.6, anchor=CENTER)

root.geometry("500x300+120+120")
root.mainloop()
