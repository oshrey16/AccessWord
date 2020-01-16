import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import Listbox
from tkinter import colorchooser
from datetime import date
import pyperclip

loguser = ''
logusertype = ''
c_options = dict()
k_width = 0
k_height = 0


# ====================================Register==========================================
def user_Register(disability):
    root = tk.Toplevel()
    root.title("AccessWord: Register User")
    width = 550
    height = 500
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
    PHONE = StringVar()

    # ==============================METHODS========================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `User_Blind` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT , age TEXT, email TEXT, phone TEXT)")
        cursor.execute(
            "SELECT * FROM `User_Blind` WHERE `username` = 'admin' AND `password` = 'admin' AND `age` = 'admin' AND `email` = 'admin' AND `phone` = 'admin'")

    def Register(event=None):
        global c_options
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "" or PASSWORD2.get() == "" or AGE.get() == "" or EMAIL.get() == "" or PHONE.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        elif PASSWORD.get() != PASSWORD2.get():
            lbl_text.config(text="Retype Password!", fg="red")
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
                    c_options = {'size': '1100x200', 'fontsize': '12', 'fontcolor': 'black', 'backcolor': 'white',
                                 'autosize': 1}  # defult options new user
                    cursor.execute(
                        "INSERT INTO `User_Blind` (username, password, age, email, phone, options) VALUES (?,?,?,?,?,?)",
                        (USERNAME.get(), PASSWORD.get(), AGE.get(), EMAIL.get(), PHONE.get(), str(c_options)))
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
                    c_options = {'size': '1100x200', 'fontsize': '12', 'fontcolor': 'black', 'backcolor': 'white',
                                 'autosize': 1}  # defult options new user
                    cursor.execute(
                        "INSERT INTO `User_Deaf` (username, password, age, email, phone, options) VALUES (?,?,?,?,?,?)",
                        (USERNAME.get(), PASSWORD.get(), AGE.get(), EMAIL.get(), PHONE.get(), str(c_options)))
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
        global loguser
        global logusertype
        loguser = USERNAME.get()
        logusertype = disability
        keyboard()

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
    lbl_phone = Label(Form, text="Phone:", font=('arial', 14), bd=15)
    lbl_phone.grid(row=5, sticky="e")
    lbl_disability = Label(Form, text="Disability:", font=('arial', 14), bd=15)
    lbl_disability.grid(row=6, sticky="e")
    lbl_disabilityshow = Label(Form, text=disability, font=('arial', 14), bd=15)
    lbl_disabilityshow.grid(row=6, column=1)
    lbl_text = Label(Form)
    lbl_text.grid(row=7, columnspan=2)

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
    phone = Entry(Form, textvariable=PHONE, font=(14))
    phone.grid(row=5, column=1)
    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Register", width=45, command=Register)
    btn_login.grid(pady=0, row=8, columnspan=3, column=0)
    btn_login.bind('<Return>', Register)


# ====================================Register==========================================
# ========================user_login_visually impaired========================
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
        global loguser
        global logusertype
        loguser = USERNAME.get()
        logusertype = 'visually impaired'
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `User_Blind`")
        record = cursor.fetchall()
        for row in record:
            if loguser == row[1]:
                global c_options
                d = eval(row[6])
                d = dict(d)  # convert to dict
                c_options = d
        keyboard()

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


# ========================user_login_Hearing impaired========================
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

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `User_Deaf` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
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
        global loguser
        global logusertype
        loguser = USERNAME.get()
        logusertype = 'Hearing impaired'
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `User_Blind`")
        record = cursor.fetchall()
        for row in record:
            if loguser == row[1]:
                global c_options
                d = eval(row[6])
                d = dict(d)  # convert to dict
                c_options = d
        keyboard()

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
        global loguser
        global c_options
        global logusertype
        loguser = USERNAME.get()
        logusertype = 'admin'
        global conn, cursor
        conn = sqlite3.connect("AdminPassword.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `Admin`")
        record = cursor.fetchall()
        for row in record:
            if loguser == row[1]:
                global c_options
                d = eval(row[6])
                d = dict(d)  # convert to dict
                c_options = d
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
        conn.close()

    def Show_reports():
        root = tk.Toplevel()
        root.title("AccessWord: Reports")
        width = 750
        height = 580
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
        lbl_title = Label(Top, text="Reports", font=('arial', 15))
        lbl_title.pack(fill=X)
        scrollbar = tk.Scrollbar(root, orient="vertical")
        listbox = tk.Listbox(root, font=('ariel', 10), width=90, height=30)
        listbox.pack(expand='yes', fill='both')
        listbox.place(relx=0.5, rely=0.5, anchor=CENTER)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.insert('end',
                       '{:20s}|{:60s}|{:15s}'.format(('UserName'), ('Report'), ('Date Of Report')))

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
def OptionsKeyboard():
    kb = tk.Toplevel()
    kb.title("KeyBoard - Options")
    width = 780
    height = 720
    screen_width = kb.winfo_screenwidth()
    screen_height = kb.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    kb.geometry("%dx%d+%d+%d" % (width, height, x, y))
    kb.resizable(0, 0)
    # ==============================FRAMES=========================================
    Top = Frame(kb, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(kb, height=200)
    Form.pack(side=TOP, pady=0)
    Form.place(relx=0.1, rely=0.1)
    # ==============================LABELS=========================================
    lbl_title = Label(Top, text="AccessWord: " + loguser + " Options", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_window_size = Label(Form, text="window size:", font=('arial', 14), bd=15)
    lbl_window_size.grid(row=0, column=0, sticky="e")
    lbl_font = Label(Form, text="font size:", font=('arial', 14), bd=15)
    lbl_font.grid(row=0, column=4, sticky="e")
    lbl_font_color = Label(Form, text="font color:", font=('arial', 14), bd=15)
    lbl_font_color.grid(row=0, column=10, sticky="e")
    lbl_back_color = Label(Form, text="backcolor:", font=('arial', 14), bd=15)
    lbl_back_color.grid(row=0, column=15, sticky="e")

    # ==============================ListBoxs=========================================
    def call_me1():
        nonlocal lbl_font_color1
        nonlocal font_color_box
        clr = colorchooser.askcolor(title="select color - font color")
        lbl_font_color1['text'] = clr[1]
        font_color_box = Entry(Form1, textvariable=font_color_boxX, font=(14), bg=lbl_font_color1['text'], width=4)
        font_color_box.grid(row=6, column=10, columnspan=3)

    def call_me2():
        nonlocal back_color_box
        nonlocal lbl_back_color1
        clr = colorchooser.askcolor(title="select color - back color")
        lbl_back_color1['text'] = clr[1]
        back_color_box = Entry(Form1, textvariable=back_color_boxX, font=(14), bg=lbl_back_color1['text'], width=4)
        back_color_box.grid(row=6, column=15, columnspan=3)

    button1 = Button(kb, text="custom color", command=call_me1)
    button1.pack()
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button2 = Button(kb, text="custom color", command=call_me2)
    button2.pack()
    button2.place(relx=0.65, rely=0.5, anchor=CENTER)

    # Get Selected Value From ListBox
    def CurSelet1(evt):
        value = listbox_window_size.get(ANCHOR)
        lbl_window_size1['text'] = value

    def CurSelet2(evt):
        value = listbox_font.get(ANCHOR)
        lbl_font1_size['text'] = value
        font_size_box.configure(font=('ariel', value))
        font_size_box.grid(row=6, column=4, columnspan=3)

    def CurSelet3(evt):
        value = listbox_font_color.get(ANCHOR)
        lbl_font_color1['text'] = value
        font_color_box = Entry(Form1, textvariable=font_color_boxX, font=(14), bg=lbl_font_color1['text'], width=4)
        font_color_box.grid(row=6, column=10, columnspan=3)

    def CurSelet4(evt):
        value = listbox_backcolor.get(ANCHOR)
        lbl_back_color1['text'] = value
        back_color_box = Entry(Form1, textvariable=back_color_boxX, font=(14), bg=lbl_back_color1['text'], width=4)
        back_color_box.grid(row=6, column=15, columnspan=3)

    def Pre_Save_Settings():
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
        save_c_options = c_options

        def NO_Save_Settings():
            Home.destroy()
            c_options = save_c_options
            kb1.destroy()

        def Yes_Save_Settings():
            Home.destroy()
            kb1.destroy()
            Save_Settings()

        lbl_home = Label(Home, text="Are you sure?", font=('times new roman', 20)).pack()
        btn_save = Button(Home, text='SAVE!', command=Yes_Save_Settings).pack()
        btn_notsave = Button(Home, text='NO!!!', command=NO_Save_Settings).pack()
        c_options['size'] = lbl_window_size1['text']
        c_options['fontsize'] = lbl_font1_size['text']
        c_options['fontcolor'] = lbl_font_color1['text']
        c_options['backcolor'] = lbl_back_color1['text']
        c_options['autosize'] = Auto_size.get()
        keyboard()

    def Save_Settings():
        c_options['size'] = lbl_window_size1['text']
        c_options['fontsize'] = lbl_font1_size['text']
        c_options['fontcolor'] = lbl_font_color1['text']
        c_options['backcolor'] = lbl_back_color1['text']
        c_options['autosize'] = Auto_size.get()
        if (logusertype == 'visually impaired'):
            global conn, cursor
            conn = sqlite3.connect("AdminPassword.db")
            cursor = conn.cursor()
            cursor.execute("""UPDATE User_Blind
            SET options=?
            WHERE username=?
            """, (str(c_options), loguser))
            conn.commit()
            conn.close()
        if (logusertype == 'Hearing impaired'):
            conn = sqlite3.connect("AdminPassword.db")
            cursor = conn.cursor()
            cursor.execute("""UPDATE User_Deaf
                    SET options=?
                    WHERE username=?
                    """, (str(c_options), loguser))
            conn.commit()
            conn.close()
        kb.destroy()
        keyboard()

    def Back_To_Keyboard():
        kb.destroy()
        keyboard()

    def Report_TO_Admin():
        root = tk.Toplevel()
        root.title("AccessWord: Report Problem")
        width = 550
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        USERNAME = StringVar()
        DATE = StringVar()
        MESSAGE = StringVar()

        # ==============================FRAMES=========================================
        Top = Frame(root, bd=2, relief=RIDGE)
        Top.pack(side=TOP, fill=X)
        Form = Frame(root, height=200)
        Form.pack(side=TOP, pady=20)

        # ==============================LABELS=========================================
        lbl_title = Label(Top, text="AccessWord: Report Problem", font=('arial', 15))
        lbl_title.pack(fill=X)
        lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
        lbl_username.grid(row=0, sticky="e")
        lbl_password = Label(Form, text="Date:", font=('arial', 14), bd=15)
        lbl_password.grid(row=1, sticky="e")
        lbl_password2 = Label(Form, text="Messege:", font=('arial', 14), bd=15)
        lbl_password2.grid(row=2, sticky="e")

        global date
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")

        username = Entry(Form, textvariable=USERNAME, font=(14), state=DISABLED)
        username.grid(row=0, column=1)
        USERNAME.set(loguser)
        date = Entry(Form, textvariable=DATE, font=(14), state=DISABLED)
        date.grid(row=1, column=1)
        DATE.set(d1)
        mess = Entry(Form, textvariable=MESSAGE, font=(14))
        mess.grid(row=2, column=1)
        mess.config(width=30)
        mess.config(height=30)

    listbox_window_size = tk.Listbox(kb, font=('ariel', 10), width=10, height=10)
    listbox_window_size.pack(expand='yes', fill='both')
    listbox_window_size.place(relx=0.2, rely=0.32, anchor=CENTER)
    listbox_window_size.insert('end', '1100x200', '1100x400', '1100x600', '1200x700')
    listbox_window_size.bind('<<ListboxSelect>>', CurSelet1)
    listbox_font = tk.Listbox(kb, font=('ariel', 10), width=10, height=10)
    listbox_font.pack(expand='yes', fill='both')
    listbox_font.place(relx=0.34, rely=0.32, anchor=CENTER)
    listbox_font.insert('end', '8', '10', '12', '14', '16', '20', '24', '28', '32')
    listbox_font.bind('<<ListboxSelect>>', CurSelet2)
    listbox_font_color = tk.Listbox(kb, font=('ariel', 10), width=10, height=10)
    listbox_font_color.pack(expand='yes', fill='both')
    listbox_font_color.place(relx=0.5, rely=0.32, anchor=CENTER)
    listbox_font_color.insert('end', 'black', 'red', 'blue', 'white', 'green')
    listbox_font_color.bind('<<ListboxSelect>>', CurSelet3)
    listbox_backcolor = tk.Listbox(kb, font=('ariel', 10), width=10, height=10)
    listbox_backcolor.pack(expand='yes', fill='both')
    listbox_backcolor.place(relx=0.65, rely=0.32, anchor=CENTER)
    listbox_backcolor.insert('end', 'black', 'red', 'blue', 'white', 'green')
    listbox_backcolor.bind('<<ListboxSelect>>', CurSelet4)

    Auto_size = IntVar()
    auto_size = Checkbutton(kb, text="Auto Size", variable=Auto_size)
    auto_size.pack()
    auto_size.place(relx=0.2, rely=0.45, anchor=CENTER)

    # ==============================LABELS Corrent Options=========================================

    Form1 = Frame(kb, height=200)
    Form1.pack(side=TOP, pady=0)
    Form1.place(relx=0.1, rely=0.55)
    lbl_cur_options = Label(Form1, text="Current options:", font=('arial', 16), bd=15)
    lbl_cur_options.grid(row=0, column=0, sticky="e", columnspan=15)
    lbl_window_size = Label(Form1, text="window size:", font=('arial', 14), bd=15)
    lbl_window_size.grid(row=4, column=0, sticky="e")
    lbl_font = Label(Form1, text="font size:", font=('arial', 14), bd=15)
    lbl_font.grid(row=4, column=4, sticky="e")
    lbl_font_color = Label(Form1, text="font color:", font=('arial', 14), bd=15)
    lbl_font_color.grid(row=4, column=10, sticky="e")
    lbl_back_color = Label(Form1, text="backcolor:", font=('arial', 14), bd=15)
    lbl_back_color.grid(row=4, column=15, sticky="e")

    lbl_window_size1 = Label(Form1, text="NULL", font=('arial', 14), bd=15)
    lbl_window_size1.grid(row=8, column=0, sticky="e")
    lbl_font1_size = Label(Form1, text="NULL", font=('arial', 14), bd=15)
    lbl_font1_size.grid(row=8, column=4, sticky="e")
    lbl_font_color1 = Label(Form1, text='NULL', font=('arial', 14), bd=15)
    lbl_font_color1.grid(row=8, column=10, sticky="e")
    lbl_back_color1 = Label(Form1, text="NULL", font=('arial', 14), bd=15)
    lbl_back_color1.grid(row=8, column=15, sticky="e")

    Form2 = Frame(kb, height=300)
    Form2.pack(side=TOP, pady=0)
    Form2.place(relx=0.3, rely=0.85)

    btn_save = Button(Form2, text="Save Settings", width=35, height=3, command=Pre_Save_Settings)
    btn_save.grid(pady=0, row=0, column=0)
    btn_report = Button(Form2, text="Report Problem", width=15, command=Report_TO_Admin)
    btn_report.grid(pady=0, row=5, column=0)
    btn_report = Button(Form2, text="BACK", width=15, command=Back_To_Keyboard)
    btn_report.grid(pady=0, row=5, column=7)

    #####LOAD OPTION FOR USER
    global conn, cursor
    conn = sqlite3.connect("AdminPassword.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `User_Blind`")
    record = cursor.fetchall()
    for row in record:
        if loguser == row[1]:
            global c_options
            d = eval(row[6])
            d = dict(d)  # convert to dict
            c_options = d
            lbl_window_size1['text'] = d['size']
            lbl_font1_size['text'] = d['fontsize']
            lbl_font_color1['text'] = d['fontcolor']
            lbl_back_color1['text'] = d['backcolor']
            Auto_size.set(d['autosize'])

    #######BOX COLOR INDICATION#######
    font_size_boxX = StringVar()
    font_size_box = Entry(Form1, textvariable=font_size_boxX, font=lbl_font1_size['text'], width=4)
    font_size_box.grid(row=6, column=4, columnspan=3)
    font_size_boxX.set('abc')
    font_color_boxX = StringVar()
    font_color_box = Entry(Form1, textvariable=font_color_boxX, font=(14), bg=lbl_font_color1['text'], width=4)
    font_color_box.grid(row=6, column=10, columnspan=3)
    back_color_boxX = StringVar()
    back_color_box = Entry(Form1, textvariable=back_color_boxX, font=(14), bg=lbl_back_color1['text'], width=4)
    back_color_box.grid(row=6, column=15, columnspan=3)


def select(value):
    if value == "BACK":
        entry.delete(len(entry.get()) - 1, END)

    elif value == "SPACE":
        entry.insert(END, ' ')
    elif value == " Tab ":
        entry.insert(END, '    ')
    else:
        entry.insert(END, value)


def HosoPop(kb, entry):
    def OptionsKeyboard_open():
        kb.destroy()
        OptionsKeyboard()

    def Copy_Text():
        pyperclip.copy(entry.get())  # Copy to clipboard

    def Clear():
        entry.delete('0', 'end')

    varRow = 2
    varColumn = 0
    font_color = c_options['fontcolor']
    back_color = c_options['backcolor']
    font_size = int(c_options['fontsize'])
    row_space = 5
    space_span = 11
    font_size_space = font_size
    font_size_options = font_size
    if (font_size >= 20):
        global buttons
        row_space = 8
        buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                   'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   '-', '[', ']', '+', ',', '.', '?', 'SHIFT', '/', 'Space', 'Clear', 'Copy Text', 'Options']
        if font_size >= 24:
            space_span = 8
            font_size_space = 20
            font_size_options = 20
            if font_size == 28:
                space_span = 10
            if font_size == 32:
                space_span = 8

    for button in buttons:

        command = lambda x=button: select(x)

        if button == "Space":
            Button(kb, text=button, width=70, bg=back_color, fg=font_color,
                   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, font=('ariel', font_size_space), command=lambda x=button: select(" ")).grid(
                row=row_space, column=0, columnspan=space_span)
        elif button == "Copy Text":
            Button(kb, text=button, width=10, bg="#6D6D6D", fg="#0007AB",
                   activebackground="#000000", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, font=('ariel', font_size_options), command=Copy_Text).grid(row=2, column=16)
        elif button == "Clear":
            Button(kb, text=button, width=10, bg="#6D6D6D", fg="#0007AB",
                   activebackground="#000000", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, font=('ariel', font_size_options), command=Clear).grid(row=3, column=16)
        elif button == "Options":
            Button(kb, text=button, width=10, bg="#6D6D6D", fg="#0007AB",
                   activebackground="#000000", activeforeground="#3c4987", relief='raised', padx=10,
                   pady=1, bd=2, font=('ariel', font_size_options), command=OptionsKeyboard_open).grid(row=4, column=16)
        else:
            Button(kb, text=button, width=5, bg=back_color, fg=font_color,
                   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=4,
                   pady=4, bd=2, command=command, font=('ariel', font_size)).grid(row=varRow, column=varColumn)

        varColumn += 1

        if font_size == 20:
            if varColumn > 11:
                varColumn = 0
                varRow += 1
        elif font_size == 24:
            if varColumn > 7:
                varColumn = 0
                varRow += 1
        elif font_size == 28:
            if varColumn > 9:
                varColumn = 0
                varRow += 1
        elif font_size == 32:
            if varColumn > 8:
                varColumn = 0
                varRow += 1
        else:
            if varColumn > 14 and varRow == 2:
                varColumn = 0
                varRow += 1
            if varColumn > 14 and varRow == 3:
                varColumn = 0
                varRow += 1


def keyboard():
    global k_width
    global k_height
    global kb1
    kb1 = Toplevel()
    kb1.title("AccessWord: Keyboard")
    kb1.resizable(0, 0)
    xx = ""
    xx = str(c_options['size']).split("x")
    width = int(xx[0])
    height = int(xx[1])
    screen_width = kb1.winfo_screenwidth()
    screen_height = kb1.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    font_size = c_options['fontsize']
    auto_size = c_options['autosize']
    if (auto_size == 1):
        if int(font_size) == 14:
            width = 1220
            height = 240
        elif (int(font_size) == 16):
            width = 1320
            height = 250
        elif (int(font_size) == 18):
            width = 1450
            height = 250
        elif (int(font_size) == 20):
            width = 1440
            height = 370
        elif (int(font_size) == 24):
            width = 1360
            height = 540
        elif (int(font_size) == 28):
            width = 1460
            height = 540
        elif (int(font_size) == 32):
            width = 1500
            height = 630
    k_width = width
    k_height = height
    kb1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # kb.configure(bg='black')
    global entry
    entry = Entry(kb1, width=128)
    entry.grid(rowspan=1, columnspan=15, ipadx=100, ipady=20)
    lbl_name = Label(kb1, text="Hello " + loguser, font=('arial', font_size), bd=15)
    lbl_name.grid(row=0, column=16, sticky="e")
    # entry.pack()
    HosoPop(kb1, entry)


buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
           'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
           'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', 'SHIFT', '1', '2', '3', '/',
           'Space', 'Clear', 'Copy Text', 'Options']


# Main Window #
def Main():
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


if __name__ == '__main__':
    Main()
