import pygame
import pygame-menu
import sqlite3 as sql


# from main import b



class Account():
    def __init__(self):
        self.loggedin = False
        self.ID = -1

    def createDB(self):
        conn = sql.connect('logins2.db')
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS logins
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        username CHAR(20) NOT NULL,
                        password CHAR(20) NOT NULL)
                        """)
        conn.commit()
        cur.close()
        conn.close()

    def deleteAll(self):
        conn = sql.connect('logins2.db')
        conn.execute("DROP TABLE logins")
        conn.commit()
        conn.close()

    def deleteEmpty(self):
        conn = sql.connect('logins2.db')
        conn.execute("DELETE FROM logins WHERE ID > 2")
        conn.commit()
        conn.close()

    def createAccount(self, username, password):
        conn = sql.connect('logins2.db')
        conn.execute("INSERT INTO logins (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        print("Account has been created successfully.")

    def login(self, username, password):
        conn = sql.connect('logins2.db')
        cur = conn.cursor()
        cur.execute("SELECT ID from logins WHERE username = ? and password = ?", (username, password))
        a = cur.fetchone()
        if a == None:
            print("Your details are incorrect or not in our database.")
        else:
            print("You're logged in with ID:", a[0])
            self.ID = a[0]
            self.loggedin = True
            side.destroy()
            gui.mainInterface()
        cur.close()
        conn.close()

    def printDB(self):
        if self.ID == 1:
            conn = sql.connect('logins2.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM logins")
            print(cur.fetchall())
            conn.commit()
            conn.close()
        else:
            print("You do not have the permission for this.")

    def logout(self):
        self.loggedin = False
        self.ID = -1
        print("You have successfully logged out.")




class GUI:
    def __init__(self):
        pass

    def basicInterface(self):
        basic = Tk()
        basic.title("Basic Interface")

        basic.geometry('300x50')

        quitB = Button(basic, text="Quit", command=basic.destroy)
        quitB.place(height=50, width=100, x=200, y=0)

        createB = Button(basic, text="Create an Account", command=lambda: [basic.destroy(), self.accountCreation()])
        createB.place(height=50, width=100, x=100, y=0)

        loginB = Button(basic, text="Login", command=lambda: [basic.destroy(), self.loginAccount()])
        loginB.place(height=50, width=100, x=0, y=0)

        basic.mainloop()

    def accountCreation(self):
        side = Tk()
        side.title("Create an Account")

        side.geometry('300x100')

        usernameE = Entry(side, width=15)
        usernameE.place(x=0, y=25)
        usernameL = Label(side, text="Username")
        usernameL.place(x=0, y=0)

        passwordE = Entry(side, width=14)
        passwordE.place(x=100, y=25)
        passwordL = Label(side, text="Password")
        passwordL.place(x=100, y=0)

        backB = Button(side, text="Back", command=lambda: [side.destroy(), self.basicInterface()])
        backB.place(height=50, width=100, x=0, y=50)

        enterB = Button(side, text="Enter",
                        command=lambda: [ac.createAccount(usernameE.get(), passwordE.get()), side.destroy(),
                                         self.basicInterface()])
        enterB.place(height=50, width=100, x=100, y=50)

        side.mainloop()

    def loginAccount(self):
        global side
        side = Tk()
        side.title("Login")

        side.geometry('300x100')

        usernameE = Entry(side, width=15)
        usernameE.place(x=0, y=25)
        usernameL = Label(side, text="Username")
        usernameL.place(x=0, y=0)

        passwordE = Entry(side, width=15)
        passwordE.place(x=100, y=25)
        passwordL = Label(side, text="Password")
        passwordL.place(x=100, y=0)

        backB = Button(side, text="Back", command=lambda: [side.destroy(), self.basicInterface()])
        backB.place(height=50, width=100, x=0, y=50)

        enterB = Button(side, text="Enter", command=lambda: [ac.login(usernameE.get(), passwordE.get())])
        enterB.place(height=50, width=100, x=100, y=50)

        side.mainloop()

    def mainInterface(self):
        main = Tk()
        main.title("Main Interface")

        main.geometry('600x400')

        logoutB = Button(main, text="Logout", command=lambda: [main.destroy(), ac.logout(), self.basicInterface()])
        logoutB.place(height=50, width=100, x=200, y=350)

        if ac.ID == 1:
            pDB = Button(main, text="Print Database", command=lambda: [ac.printDB()])
            pDB.place(height=50, width=100, x=400, y=350)

            play = Button(main, text="Find Game", command=lambda: [playgame()])
            play.place(height=50, width=100, x=100, y=350)

            pS = Button(main, text="Print Scoreboard", command=lambda: [print("Scoreboard")])
            pS.place(height=50, width=100, x=300, y=350)
        else:
            play = Button(main, text="Find Game", command=lambda: [playgame()])
            play.place(height=50, width=100, x=100, y=350)

            pS = Button(main, text="Print Scoreboard", command=lambda: [print("Scoreboard")])
            pS.place(height=50, width=100, x=300, y=350)



class Menus():
  def __init__(self):
    self.myimage = pygame_menu.baseimage.BaseImage(
    image_path="bgImage.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER,
    offset=(0,0))
    
    self.mytheme = Theme(background_color=self.myimage, # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                widget_padding=25)

  def loginMenu(self):
    loginmenu = pygame_menu.Menu('Log In',
                                800,
                                800,
                                theme=self.mytheme)


    loginmenu.add.text_input("Username: ", default="JohnDoe1999")
    loginmenu.add.text_input("Password: ", password=True)
    
    loginmenu.add.button('Log In', self.pawnChange)
    loginmenu.add.button('Exit', self.pawnChange)

    loginmenu.mainloop(screen)

  def signupMenu(self):
    signupmenu = pygame_menu.Menu('Log In',
                                800,
                                800,
                                theme=self.mytheme)


    loginmenu.add.text_input("Username: ", default="JohnDoe1999")
    loginmenu.add.text_input("Password: ", password=True)
    
    loginmenu.add.button('Log In', self.pawnChange)
    loginmenu.add.button('Exit', self.pawnChange)

    loginmenu.mainloop(screen)

  

  def mainMenu(self):
    mainmenu = pygame_menu.Menu('Main Menu',
                                800,
                                800,
                                theme=self.mytheme)

    mainmenu.add.button('Log In', self.pawnChange)
    mainmenu.add.button('Sign Up', self.pawnChange)
    mainmenu.add.button('View Leaderboards', self.pawnChange)
    mainmenu.add.button('Exit', self.pawnChange)

    mainmenu.mainloop(screen)

ac = Account()
gui = GUI()

