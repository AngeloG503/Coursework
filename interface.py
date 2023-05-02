import pygame_menu
import pygame
from gameFile import Board
import sqlite3 as sql
from gameFile import b

# from main import b


class Stats():
    def __init__(self):
        self.ID = -1

    def createDB(self):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS stats
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        elo INT(4) NOT NULL DEFAULT 1000,
                        wins INT(20) NOT NULL DEFAULT 0,
                        loss INT(20) NOT NULL DEFAULT 0,
                        draw INT(20) NOT NULL DEFAULT 0)
                        """)
        conn.commit()
        cur.close()
        conn.close()

    def printDB(self):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM stats")
        print(cur.fetchall())
        conn.commit()
        conn.close()


    def eloGrabber(self):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute(
            "SELECT elo from stats WHERE fID = ?",
            (self.ID,))
        a = cur.fetchone()
        return a[0]

log = Stats()


class Account():
    def __init__(self):
        self.loggedin = False
        self.ID = -1
        self.admin = False
        self.elo = None

    def createDB(self):
        conn = sql.connect('database.db')
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
        conn = sql.connect('database.db')
        conn.execute("DROP TABLE logins")
        conn.commit()
        conn.close()

    def deleteEmpty(self):
        conn = sql.connect('database.db')
        conn.execute("DELETE FROM logins WHERE ID > 2")
        conn.commit()
        conn.close()

    def createAccount(self, username, password):
        conn = sql.connect('database.db')
        conn.execute("INSERT INTO logins (username, password) VALUES (?, ?)",
                     (username, password))

        conn.execute("INSERT INTO stats (username) VALUES (?)", (username,))
        conn.commit()
        conn.close()
        print("Account has been created successfully.")

    def login(self, username, password):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute(
            "SELECT ID from logins WHERE username = ? and password = ?",
            (username, password))
        a = cur.fetchone()
        if a == None:
            print("Your details are incorrect or not in our database.")
            cur.close()
            conn.close()
            return False
        else:
            print("You're logged in with ID:", a[0])
            self.ID = a[0]
            self.loggedin = True
            cur.execute(
            "SELECT admin from logins WHERE ID = ?",(self.ID,))
            b = cur.fetchone()
            if b[0] == 1:
                self.admin = True
            log.ID = self.ID
            self.elo = log.eloGrabber()
            cur.close()
            conn.close()
            return True




    def printDB(self):
        if self.ID == 1:
            conn = sql.connect('database.db')
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
        log.ID = -1
        print("You have successfully logged out.")

class Menus():

    def __init__(self, accountVar):
        # self.myimage = pygame_menu.baseimage.BaseImage(
        #     image_path="bgImage.png",
        #     drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER)

        self.winner = None
        self.mytheme = pygame_menu.Theme(
            background_color=(6, 199, 169, 201),  # transparent background
            title_background_color=(4, 47, 126),
            title_font_shadow=True,
            widget_padding=25)

        self.ac = accountVar
        self.screen = None
        self.mainmenu = None
        self.difficulty = None

    def signup(self, username, password):
        usernameT = username.get_value()
        passwordT = password.get_value()
        self.ac.createAccount(usernameT, passwordT)
        return pygame_menu.events.BACK

    def login(self, username, password, menu):
        passwordT = username.get_value()
        usernameT = password.get_value()
        if self.ac.login(usernameT, passwordT):
            menu.disable()

    def logout(self, menu, menu2):
        self.ac.logout()
        menu.enable()
        menu2.disable()

    def startGame(self, menu, menu2):
        b = Board(self)
        b.openg()
        menu.enable()
        menu2.disable()

    def startGameC(self, menu, menu2):
        b = Board(self)
        b.opengC(self.difficulty, self.ac.elo)
        menu.enable()
        menu2.disable()

    def change_difficulty(self, tuple, difficulty):
        self.difficulty = difficulty


    def mainLoop(self):
        pygame.init()  # Initialise pygame
        self.screen = pygame.display.set_mode([800, 800])

        adminmenu = pygame_menu.Menu('Admin Menu', 800, 800, theme=self.mytheme)
        gamemenu = pygame_menu.Menu('Game Menu', 800, 800, theme=self.mytheme)
        mainmenu = pygame_menu.Menu('Main Menu', 800, 800, theme=self.mytheme)
        signupmenu = pygame_menu.Menu('Sign Up', 800, 800, theme=self.mytheme)
        loginmenu = pygame_menu.Menu('Log In', 800, 800, theme=self.mytheme)
        selectmenu = pygame_menu.Menu('Select Mode', 800, 800, theme=self.mytheme)
        endmenu = pygame_menu.Menu('Game Over', 800, 800, theme=self.mytheme)
        
        loginUsernameInput = loginmenu.add.text_input(
            "Username: ")
        loginPasswordInput = loginmenu.add.text_input(
            "Password: ",
            password=True)
        loginmenu.add.button('Log In', self.login, loginPasswordInput, loginUsernameInput, mainmenu)
        loginmenu.add.button('Back', pygame_menu.events.BACK)
        loginmenu.disable()
        
        signUsernameInput = signupmenu.add.text_input(
            "Username: ")
        signPasswordInput = signupmenu.add.text_input(
            "Password: ",
            password=True)
        signupmenu.add.button('Sign Up', self.signup, signUsernameInput,
                              signPasswordInput)
        signupmenu.add.button('Back', pygame_menu.events.BACK)
        signupmenu.disable()

        
        mainmenu.add.button('Log In', loginmenu)
        mainmenu.add.button('Sign Up', signupmenu)
        mainmenu.add.button('View Leaderboards', print, "leaderboards")
        mainmenu.add.button('Exit', pygame_menu.events.EXIT)
        mainmenu.enable()

        gamemenu.add.button('Find Game', selectmenu)
        gamemenu.add.button('Log Out', self.logout, mainmenu, gamemenu)
        gamemenu.add.button('View Leaderboards', print, "leaderboards")
        gamemenu.add.button('Exit', pygame_menu.events.EXIT)
        gamemenu.disable()

        adminmenu.add.button('View Leaderboards', print, "leaderboards")
        adminmenu.add.button('View Leaderboards', print, "leaderboards")
        adminmenu.add.button('View Leaderboards', print, "leaderboards")
        adminmenu.add.button('Back', pygame_menu.events.BACK)
        adminmenu.disable()

        items = [('Easy', 'EASY'), ('Normal', 'NORMAL'), ('Hard', 'HARD'), ('Impossible', 'DEAD')]
        selectmenu.add.selector('Difficulty', items, onchange=self.change_difficulty)
        selectmenu.add.button('Find Game', self.startGameC, endmenu, selectmenu)
        selectmenu.add.label('OR')
        selectmenu.add.button('Play vs Friend', self.startGame, endmenu, selectmenu)
        selectmenu.disable()


        winningmessage = "Game Over, winner is ", self.winner, "!"
        elochange = "Your new elo is "
        endmenu.add.label(winningmessage)
        endmenu.add.label(elochange)
        endmenu.add.button('Play Again', self.startGame, endmenu, gamemenu)
        endmenu.add.button('Back', pygame_menu.events.BACK)
        endmenu.add.button('Exit', pygame_menu.events.EXIT)
        endmenu.disable()

      
        running = True
        events = pygame.event.get()
      
        while running:  # While loop to close game when user quits
            for event in events:
                if event.type == pygame.QUIT:  # User clicking the close button
                    running = False

            if self.ac.loggedin:
                if self.ac.ID == 1:
                    gamemenu.add.button('Admin Menu', adminmenu)
              
                gamemenu.enable()
                gamemenu.mainloop(self.screen)              
                  
            elif mainmenu.is_enabled():
                mainmenu.full_reset()
                mainmenu.mainloop(self.screen)
                    
            pygame.display.update()
