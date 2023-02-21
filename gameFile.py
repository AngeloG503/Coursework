import pygame
import pygame_menu
from pieces import Pawn, King, Queen, Bishop, Horse, Rook

wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8 = Pawn("white", "wP.png", (9, 600, 100, 100)), Pawn("white", "wP.png", (
    109, 600, 100, 100)), Pawn("white",
                               # Creates white pawns
                               "wP.png", (209, 600, 100, 100)), Pawn(
    "white", "wP.png", (309, 600, 100, 100)), Pawn("white", "wP.png", (409, 600, 100, 100)), Pawn("white",
                                                                                                        "wP.png", (
                                                                                                            509, 600,
                                                                                                            100,
                                                                                                            100)), Pawn(
    "white", "wP.png", (609, 600, 100, 100)), Pawn(
    "white", "wP.png", (709, 600, 100, 100))

bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8 = Pawn("black", "bP.png", (9, 100, 100, 100)), Pawn("black", "bP.png", (
    109, 100, 100, 100)), Pawn("black",
                               # Creates black pawns
                               "bP.png", (209, 100, 100, 100)), Pawn(
    "black", "bP.png", (309, 100, 100, 100)), Pawn("black", "bP.png", (409, 100, 100, 100)), Pawn("black",
                                                                                                        "bP.png", (
                                                                                                            509, 100,
                                                                                                            100,
                                                                                                            100)), Pawn(
    "black", "bP.png", (609, 100, 100, 100)), Pawn(
    "black", "bP.png", (709, 100, 100, 100))

bK1, wK1, bQ1, wQ1 = King("black", "bK.png", (409, 5, 0, 0)), King("white", "wK.png", (409, 705, 0, 0)), Queen(
    "black", "bQ.png", (309, 5, 0, 0)), Queen("white",
                                                 # Creates kings and queens
                                                 "wQ.png", (309, 705, 0, 0))

bR1, bR2, wR1, wR2 = Rook("black", "bR.png", (8, 7, 100, 100)), Rook("black", "bR.png", (708, 7, 100, 100)), Rook(
    "white", "wR.png", (8, 705, 100, 100)), Rook("white",
                                                    "wR.png", (708, 705, 100, 100))  # Creates rooks

bB1, bB2, wB1, wB2 = Bishop("black", "bB.png", (207, 5, 0, 0)), Bishop("black", "bB.png", (507, 5, 0, 0)), Bishop(
    "white", "wB.png", (207, 705, 0, 0)), Bishop(
    "white", "wB.png", (507, 705, 0, 0))  # Creates bishops

bH1, bH2, wH1, wH2 = Horse("black", "bH.png", (109, 5, 0, 0)), Horse("black", "bH.png", (609, 5, 0, 0)), Horse(
    "white", "wH.png", (109, 705, 0, 100)), Horse(
    "white", "wH.png", (609, 705, 0, 0)),  # Creates horses

#  Sorting pieces into arrays
pawns = [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8,
         bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8,
         ]
rooks = [bR1, bR2, wR1, wR2]
bishops = [bB1, bB2, wB1, wB2]
horses = [bH1, bH2, wH1, wH2]

startingPosBlack = [bR1, bH1, bB1, bQ1, bK1, bB2, bH2, bR2]
startingPosWhite = [wR1, wH1, wB1, wQ1, wK1, wB2, wH2, wR2]

white = (0, 0, 0)
black = (255, 255, 255)
dbrown = (81, 42, 42)
lbrown = (124, 76, 62)
lblue = (100, 198, 255)

class Square:
    def __init__(self, row, column, width):
        self.row = row  # row for the "square"
        self.column = column  # column for the "square"
        self.x = int(row * width)  # x co-ordinate for the "square"
        self.y = int(column * width)  # y co-ordinate for the "square"
        self.colour = lbrown  # Default colour for a "square", changed when created


class Board:  # Class for any boards being created
    def __init__(self):
        self.grid = []  # Holds each separate "square" and allows for data to be stored within this
        self.board = [[None for _ in range(8)] for _ in range(8)]  # 3D array used as the board
        self.turn = 0
        self.promotion = False

        for x in range(8):  # Sets the board up to have the pieces in the correct places
            self.board[1][x] = pawns[x + 8]
            self.board[6][x] = pawns[x]

        self.board[0] = startingPosBlack
        self.board[7] = startingPosWhite

    def printboard(self):  # For testing purposes
        for x in range(8):
            print(self.board[x])

    def printgrid(self):  # For testing purposes
        for x in range(8):
            print(self.grid[x])

    def creategrid(self):
        width = 100  # Each "square" will be this size, for simplicity.
        for x in range(8):
            self.grid.append([])  # Creates 8 rows
            for y in range(8):
                self.grid[x].append(Square(x, y, width))  # For each space within a row it creates a "square"
                if (x + y) % 2 == 1:
                    self.grid[x][y].colour = dbrown  # Creates the on and off pattern of a chessboard
        return self.grid

    def refresh(self, grid):  # Runs at the end of each loop to update pygame
        for row in grid:
            for pos in row:  # Runs through every square
                self.draw(pos.colour, pos.y, pos.x)
                self.setup(pos)
        self.gridlines()
        pygame.display.update()  # pygame update

    def draw(self, colour, x, y):
        pygame.draw.rect(self.screen, colour, (x, y, 100, 100))  # Draws the square

    def setup(self, pos):
        if self.board[pos.row][pos.column] is not None and self.board[pos.row][pos.column] != "x":  # Checks whether
            # there is a piece in the square or not
            self.board[pos.row][pos.column].x = pos.column  # Changes the coordinates based on the piece
            self.board[pos.row][pos.column].y = pos.row
            self.board[pos.row][pos.column].rect = pygame.Rect(self.board[pos.row][pos.column].x * 100 + 9,
                                                               self.board[pos.row][pos.column].y * 100, 100, 100)
            self.screen.blit(self.board[pos.row][pos.column].image,
                             self.board[pos.row][pos.column].rect)  # Draws the piece
        else:
            pass

    def locatesquare(self, pos):  # Locates which square the mouse is in
        width = 100
        y, x = pos
        rows = y // width  # divides the coordinates of the mouse by 100 (width of the squares) to determine position
        columns = x // width
        return int(rows), int(columns)

    def posmovesSel(self, piece):  # Takes selected piece and marks all possible moves.
        possible = piece.possible(self.board)
        print(possible)
        for pos in possible:  # Loops through the array that holds all possible moves
            if self.board[pos[0]][pos[1]] is None:
                self.board[pos[0]][pos[1]] = 'x'  # The symbol used to mark an empty space as a possible move
            else:
                self.board[pos[0]][pos[1]].killable = True  # Marking a killable piece as such
        return possible

    def visible(self, moves):
        for pos in moves:  # Loops through the possible moves array and changes the colour of each square
            x, y = pos
            self.grid[x][y].colour = lblue

    def gridlines(self):
        width = 100
        for x in range(8):  # Loops 8 times and draws 8 lines both vertically and horizontally to outline the squares
            pygame.draw.line(self.screen, dbrown, (0, x*width), (800, x*width))
            pygame.draw.line(self.screen, dbrown, (x*width, 0), (x*width, 800))

    def move(self, startpos, endpos):
        start2, start1 = startpos  # Moves the positions from a tuple to variables to make them more accessible
        end1, end2 = endpos

        self.board[end1][end2] = self.board[start1][start2]  # Changes the end square to contain the piece
        self.board[start1][start2] = None  # Changes previous square to nothing
        self.board[end1][end2].moveCount += 1  # Adds one to the move count
        print("Moved. (Debugging purposes DO NOT LEAVE IN FINAL PRODUCT)")

    def resetgrid(self):  # Loops through the board and essentially just makes sure the colour of each square is default
        for z in range(8):
            for q in range(8):
                if (z + q) % 2 == 0:
                    self.grid[z][q].colour = lbrown
                else:
                    self.grid[z][q].colour = dbrown

                if self.board[z][q] == 'x':  # These if statements check for possible moves and removes them.
                    self.board[z][q] = None
                elif self.board[z][q] == None:
                    pass
                else:
                    self.board[z][q].killable = False

    def checkPawn(self):
        pos = (None, None)
        for z in range(8):  # Checks if there are any pawns in the final rows.
            if str(type(self.board[0][z])) == "<class 'pieces.Pawn'>":  # Checks whether the piece is or isn't a pawn.
                self.promotion = True  # Initiates pawn change function
                pos = (z, 0)  # Returns pos of pawn
                break
            elif str(type(self.board[7][z])) == "<class 'pieces.Pawn'>":  # Checks whether the piece is or isn't a pawn.
                self.promotion = True  # Initiates pawn change function
                pos = (z, 0)  # Returns pos of pawn
                break

        return pos


    def pawnChange(self, choice, pos):
        y, x = pos[1], pos[0]
        if self.board[y][x].team == "black":
            if choice == "Queen":
                name = Queen("white", "bQ.png", self.board[y][x].rect)  # Creates a new class for the new queen.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Rook":
                name = Rook("white", "bR.png", self.board[y][x].rect)  # Creates a new class for the new rook.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Horse":
                name = Horse("white", "bH.png", self.board[y][x].rect)  # Creates a new class for the new horse.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Bishop":
                name = Bishop("white", "bB.png", self.board[y][x].rect)  # Creates a new class for the new bishop.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

        elif self.board[y][x].team == "white":
            if choice == "Queen":
                name = Queen("white", "wQ.png", self.board[y][x].rect)  # Creates a new class for the new queen.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Rook":
                name = Rook("white", "wR.png", self.board[y][x].rect)  # Creates a new class for the new rook.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Horse":
                name = Horse("white", "wH.png", self.board[y][x].rect)  # Creates a new class for the new horse.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Bishop":
                name = Bishop("white", "wB.png", self.board[y][x].rect)  # Creates a new class for the new bishop.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

    def menuPawnPromote(self, screen):
        pos = self.checkPawn()
        menu = pygame_menu.Menu('Pawn Promotion', 400, 300,
                                theme=pygame_menu.themes.THEME_BLUE)

        menu.add.button('Bishop', self.pawnChange, "Bishop", pos)
        menu.add.button('Rook', self.pawnChange, "Rook", pos)
        menu.add.button('Horse', self.pawnChange, "Horse", pos)
        menu.add.button('Queen', self.pawnChange, "Queen", pos)
        menu.add.button('Confirm', menu.disable)

        menu.mainloop(screen)



    def openg(self):
        pygame.init()  # Initialise pygame
        self.screen = pygame.display.set_mode([800, 800])
        grid = self.creategrid()
        picked = False  # Is there a piece picked?
        selected = (0, 0)  # Which piece is picked

        running = True
        while running:  # While loop to close game when user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # User clicking the close button
                    running = False

                elif self.promotion:
                    self.menuPawnPromote(self.screen)

                elif event.type == pygame.MOUSEBUTTONDOWN:  # User clicking anywhere on the game window
                    pos = pygame.mouse.get_pos()  # Gets the coordinates of the mouse
                    x, y = self.locatesquare(pos)  # Saves the coordinates of the square the mouse selected
                    print(x, y)  # Testing Purposes
                    if not picked:
                        if self.board[y][x] is not None:
                            if self.turn % 2 == 0 and self.board[y][x].team == "white":  # Checks if its the correct turn
                                try:
                                    self.grid[y][x].colour = lblue  # Visually represents selected square
                                    selected = (x, y)  # Changes selected square to this
                                    picked = True  # Updates picked value
                                    possible = self.posmovesSel(self.board[y][x])  # Saves possible moves to an array
                                    self.visible(possible)  # Makes the pieces visible for possible moves

                                finally:
                                    pass

                            elif self.turn % 2 == 1 and self.board[y][x].team == "black":  # Checks if its the correct turn
                                try:
                                    self.grid[y][x].colour = lblue  # Visually represents selected square
                                    selected = (x, y)  # Changes selected square to this
                                    picked = True  # Updates picked value
                                    possible = self.posmovesSel(self.board[y][x])  # Saves possible moves to an array
                                    self.visible(possible)  # Makes the pieces visible for possible moves

                                finally:
                                    pass

                            else:
                                print("It is not your turn (Debugging purposes, DO NOT LEAVE AS FINAL PRODUCT)")

                    elif self.board[y][x] is not None:  # Checks not none as all possible moves are marked.
                        try:
                            if self.board[y][x].killable:  # This is for when a piece occupies the space
                                self.move(selected, (y, x))  # Moves the piece accordingly
                                self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                self.resetgrid()
                                self.checkPawn()
                                picked = False

                            else:
                                self.resetgrid()
                                picked = False

                        except:
                            if self.board[y][x] == 'x':  # This is for when its an empty space
                                self.move(selected, (y, x))  # Moves the piece accordingly
                                self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                self.resetgrid()
                                self.checkPawn()
                                picked = False

                            else:
                                self.resetgrid()
                                picked = False

            self.refresh(grid)
