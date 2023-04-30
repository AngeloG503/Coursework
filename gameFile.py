import pygame
import pygame_menu
import copy
from stockfish import Stockfish
from pieces import Pawn, King, Queen, Bishop, Horse, Rook

wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8 = Pawn(
    "white", "wP.png",
    (9, 600, 100, 100)), Pawn("white", "wP.png", (109, 600, 100, 100)), Pawn(
    "white",
    # Creates white pawns
    "wP.png",
    (209, 600, 100, 100)), Pawn(
    "white", "wP.png", (309, 600, 100, 100)), Pawn(
    "white", "wP.png", (409, 600, 100, 100)), Pawn(
    "white", "wP.png", (509, 600, 100, 100)), Pawn(
    "white", "wP.png",
    (609, 600, 100, 100)), Pawn("white", "wP.png",
                                (709, 600, 100, 100))

bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8 = Pawn(
    "black", "bP.png",
    (9, 100, 100, 100)), Pawn("black", "bP.png", (109, 100, 100, 100)), Pawn(
    "black",
    # Creates black pawns
    "bP.png",
    (209, 100, 100, 100)), Pawn(
    "black", "bP.png", (309, 100, 100, 100)), Pawn(
    "black", "bP.png", (409, 100, 100, 100)), Pawn(
    "black", "bP.png", (509, 100, 100, 100)), Pawn(
    "black", "bP.png",
    (609, 100, 100, 100)), Pawn("black", "bP.png",
                                (709, 100, 100, 100))

bK1, wK1, bQ1, wQ1 = King("black", "bK.png", (409, 5, 0, 0)), King(
    "white", "wK.png", (409, 705, 0, 0)), Queen("black", "bQ.png",
                                                (309, 5, 0, 0)), Queen(
    "white",
    # Creates kings and queens
    "wQ.png",
    (309, 705, 0, 0))

bR1, bR2, wR1, wR2 = Rook("black", "bR.png", (8, 7, 100, 100)), Rook(
    "black", "bR.png",
    (708, 7, 100, 100)), Rook("white", "wR.png", (8, 705, 100, 100)), Rook(
    "white", "wR.png", (708, 705, 100, 100))  # Creates rooks

bB1, bB2, wB1, wB2 = Bishop("black", "bB.png", (207, 5, 0, 0)), Bishop(
    "black", "bB.png",
    (507, 5, 0, 0)), Bishop("white", "wB.png", (207, 705, 0, 0)), Bishop(
    "white", "wB.png", (507, 705, 0, 0))  # Creates bishops

bH1, bH2, wH1, wH2 = Horse("black", "bH.png", (109, 5, 0, 0)), Horse(
    "black", "bH.png",
    (609, 5, 0, 0)), Horse("white", "wH.png", (109, 705, 0, 100)), Horse(
    "white", "wH.png", (609, 705, 0, 0)),  # Creates horses

#  Sorting pieces into arrays
pawns = [
    wP1,
    wP2,
    wP3,
    wP4,
    wP5,
    wP6,
    wP7,
    wP8,
    bP1,
    bP2,
    bP3,
    bP4,
    bP5,
    bP6,
    bP7,
    bP8
]

whiteTeam = {
    wP1: 0, 0: wP1,
    wP2: 1, 1: wP2,
    wP3: 2, 2: wP3,
    wP4: 3, 3: wP4,
    wP5: 4, 4: wP5,
    wP6: 5, 5: wP6,
    wP7: 6, 6: wP7,
    wP8: 7, 7: wP8,
    wR1: 8, 8: wR1,
    wH1: 9, 9: wH1,
    wB1: 10, 10: wB1,
    wQ1: 11, 11: wQ1,
    wK1: 12, 12: wK1,
    wB2: 13, 13: wB2,
    wH2: 14, 14: wH2,
    wR2: 15, 15: wR2
}

blackTeam = {
    bP1: 0, 0: bP1,
    bP2: 1, 1: bP2,
    bP3: 2, 2: bP3,
    bP4: 3, 3: bP4,
    bP5: 4, 4: bP5,
    bP6: 5, 5: bP6,
    bP7: 6, 6: bP7,
    bP8: 7, 7: bP8,
    bR1: 8, 8: bR1,
    bH1: 9, 9: bH1,
    bB1: 10, 10: bB1,
    bQ1: 11, 11: bQ1,
    bK1: 12, 12: bK1,
    bB2: 13, 13: bB2,
    bH2: 14, 14: bH2,
    bR2: 15, 15: bR2
}

chessKey = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "1": 7,
    "2": 6,
    "3": 5,
    "4": 4,
    "5": 3,
    "6": 2,
    "7": 1,
    "8": 0
}

reversechessKeyx = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

reversechessKeyy = {
    7: 1,
    6: 2,
    5: 3,
    4: 4,
    3: 5,
    2: 6,
    1: 7,
    0: 8
}


bPieces = {
    "Pawn": "p",
    "Rook": "r",
    "Horse": "n",
    "King": "k",
    "Queen": "q",
    "Bishop": "b"
}

wPieces = {
    "Pawn": "P",
    "Rook": "R",
    "Horse": "N",
    "King": "K",
    "Queen": "Q",
    "Bishop": "B"
}

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


stockfish = Stockfish("stockfish.exe", parameters={"UCI_Elo": 1000, "Hash": 512, "Threads": 20})


class Fen:
    def __init__(self):
        self.fen = None

    def getFen(self, b):
        fen = ""
        blankCount = 0
        for z in range(8):
            for y in range(8):
                if b.board[z][y] == None:
                    blankCount += 1
                    if y == 7:
                        fen = fen + str(blankCount)
                        blankCount = 0
                elif b.board[z][y].team == "white":
                    if blankCount > 0:
                        fen = fen + str(blankCount)
                        blankCount = 0
                    fen = fen + wPieces[type(b.board[z][y]).__name__]
                elif b.board[z][y].team == "black":
                    if blankCount > 0:
                        fen = fen + str(blankCount)
                        blankCount = 0
                    fen = fen + bPieces[type(b.board[z][y]).__name__]
            if z == 7:
                pass
            else:
                fen = fen + "/"

        if b.turn % 2 == 0:
            fen = fen + " w"
        else:
            fen = fen + " b"

        fen = fen + " KQkq"

        fen = fen + " -"

        fen = fen + " 0 "

        if b.turn == 0:
            fen = fen + "1"
        else:
            fen = fen + str(b.turn)

        self.fen = fen
        return self.fen

    def printFen(self):
        print(self.fen)

    def myMoves(self, stockfishmove):
        startpos = stockfishmove[:2]
        endpos = stockfishmove[2:]

        startx, starty = chessKey[startpos[0]], chessKey[startpos[1]]
        endy, endx = chessKey[endpos[1]], chessKey[endpos[0]]

        print(stockfishmove)
        return (startx, starty), (endy, endx)

    def revMyMoves(self, startpos, endpos):
        startx, starty = str(reversechessKeyx[startpos[0]]), str(reversechessKeyy[startpos[1]])
        endx, endy = str(reversechessKeyx[endpos[1]]), str(reversechessKeyy[endpos[0]])

        move = startx + starty + endx + endy
        print(move)
        return move

    def stockfishMove(self, moveDone, stockfishclass):
        stockfishclass.stockfish.make_moves_from_current_position([moveDone])



f = Fen()

class Board:  # Class for any boards being created

    def __init__(self):
        self.winner = None
        self.grid = [
        ]  # Holds each separate "square" and allows for data to be stored within this
        self.board = [[None for _ in range(8)]
                      for _ in range(8)]  # 3D array used as the board
        self.turn = 0
        self.promotion = False  # Check if a pawn can be promoted
        self.lastPawnJump = None  # Checks for en passant possibility
        self.turnAddedPassant = 0  # Checks how long it has been since the en passant was stored in case of not using.
        self.check = False
        self.attackers = []
        self.checkmate = False

        for x in range(
                8
        ):  # Sets the board up to have the pieces in the correct places
            self.board[1][x] = pawns[x + 8]
            self.board[6][x] = pawns[x]

        self.board[0] = startingPosBlack
        self.board[7] = startingPosWhite

        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    self.board[i][j].x = j
                    self.board[i][j].y = i

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
                self.grid[x].append(
                    Square(x, y, width)
                )  # For each space within a row it creates a "square"
                if (x + y) % 2 == 1:
                    self.grid[x][
                        y].colour = dbrown  # Creates the on and off pattern of a chessboard
        return self.grid

    def refresh(self, grid):  # Runs at the end of each loop to update pygame
        for row in grid:
            for pos in row:  # Runs through every square
                self.draw(pos.colour, pos.y, pos.x)
                self.setup(pos)

        self.gridlines()
        pygame.display.update()  # pygame update

    def draw(self, colour, x, y):
        pygame.draw.rect(self.screen, colour,
                         (x, y, 100, 100))  # Draws the square

    def setup(self, pos):
        if self.board[pos.row][pos.column] is not None and self.board[pos.row][
            pos.column] != "x":  # Checks whether
            # there is a piece in the square or not
            self.board[pos.row][
                pos.
                    column].x = pos.column  # Changes the coordinates based on the piece
            self.board[pos.row][pos.column].y = pos.row
            self.board[pos.row][pos.column].rect = pygame.Rect(
                self.board[pos.row][pos.column].x * 100 + 9,
                self.board[pos.row][pos.column].y * 100, 100, 100)
            self.screen.blit(
                self.board[pos.row][pos.column].image,
                self.board[pos.row][pos.column].rect)  # Draws the piece
        else:
            pass

    def locatesquare(self, pos):  # Locates which square the mouse is in
        width = 100
        y, x = pos
        rows = y // width  # divides the coordinates of the mouse by 100 (width of the squares) to determine position
        columns = x // width
        return int(rows), int(columns)

    def ghostSave(self):
        for i in range(16):
            blackTeam[i].temppos = blackTeam[i].x, blackTeam[i].y
            blackTeam[i].tempCount = blackTeam[i].moveCount

            whiteTeam[i].temppos = whiteTeam[i].x, whiteTeam[i].y
            whiteTeam[i].tempCount = whiteTeam[i].moveCount

    def ghostReset(self):
        for i in range(16):
            blackTeam[i].x, blackTeam[i].y = blackTeam[i].temppos
            blackTeam[i].moveCount = blackTeam[i].tempCount

            whiteTeam[i].x, whiteTeam[i].y = whiteTeam[i].temppos
            whiteTeam[i].moveCount = whiteTeam[i].tempCount

    def posmovesApply(
            self, piece, moves, board):  # Takes selected piece and marks all possible moves.
        possible = moves

        if piece.team == "white":
            for pos in possible:  # Loops through the array that holds all possible moves
                if board[pos[0]][pos[1]] is None:
                    board[pos[0]][pos[
                        1]] = 'x'  # The symbol used to mark an empty space as a possible move
                else:
                    board[pos[0]][pos[
                        1]].killable = True  # Marking a killable piece as such
        elif piece.team == "black":
            for pos in possible:  # Loops through the array that holds all possible moves
                if board[pos[0]][pos[1]] is None:
                    board[pos[0]][pos[
                        1]] = 'x'  # The symbol used to mark an empty space as a possible move
                else:
                    board[pos[0]][pos[
                        1]].killable = True  # Marking a killable piece as such

    def pinnedCheck(self, piece, posmoves):
        toremove = []
        for move in posmoves:
            self.ghostSave()
            copyboard = [list(self.board[x]) for x in range(8)]
            self.resetboard(copyboard)
            self.posmovesApply(piece, posmoves, copyboard)
            self.move((piece.x, piece.y), move, copyboard, False)
            if piece.team == "white":
                if self.checkChecker(copyboard, "black"):
                    toremove.append(move)
            else:
                print(self.checkChecker(copyboard, "white"))
                if self.checkChecker(copyboard, "white"):
                    toremove.append(move)
            self.ghostReset()

        print(type(piece), posmoves, "POSSIBLE MOVES")
        print(toremove, "TO REMOVE")
        if len(toremove) > 0:
            for items in toremove:
                posmoves.remove(items)

    def posMoves(self, piece, board):
        possible = piece.possible(board)

        if isinstance(piece, Pawn):  # If the piece is a pawn then en passant is possible
            if self.lastPawnJump is not None:  # Checks to see the chances
                if piece.team == "white":  # Checks team
                    if piece.y == self.lastPawnJump[
                        0]:  # Checks if the piece is killable in relation to selected piece
                        if piece.x + 1 == self.lastPawnJump[1]:
                            possible.append(
                                (self.lastPawnJump[0] - 1,
                                 self.lastPawnJump[1]))  # Appends if it is
                        elif piece.x - 1 == self.lastPawnJump[1]:
                            possible.append(
                                (self.lastPawnJump[0] - 1,
                                 self.lastPawnJump[1]))  # Appends if it is
                else:
                    if piece.y == self.lastPawnJump[
                        0]:  # Checks if the piece is killable in relation to selected piece
                        if piece.x + 1 == self.lastPawnJump[1]:
                            possible.append(
                                (self.lastPawnJump[0] + 1,
                                 self.lastPawnJump[1]))  # Appends if it is
                        elif piece.x - 1 == self.lastPawnJump[1]:
                            possible.append(
                                (self.lastPawnJump[0] + 1,
                                 self.lastPawnJump[1]))  # Appends if it is

        self.pinnedCheck(piece, possible)

        return possible

    def visible(self, moves):
        if len(moves) > 0:
            for pos in moves:  # Loops through the possible moves array and changes the colour of each square
                x, y = pos
                self.grid[x][y].colour = lblue

    def gridlines(self):
        width = 100
        for x in range(
                8
        ):  # Loops 8 times and draws 8 lines both vertically and horizontally to outline the squares
            pygame.draw.line(self.screen, dbrown, (0, x * width),
                             (800, x * width))
            pygame.draw.line(self.screen, dbrown, (x * width, 0),
                             (x * width, 800))

    def move(self, startpos, endpos, board, realgame):
        start2, start1 = startpos  # Moves the positions from a tuple to variables to make them more accessible
        end1, end2 = endpos

        if isinstance(board[start1][start2], Pawn):  # Begins check for en passant
            if abs(start1 -
                   end1) == 2:  # Checks whether the move was a first pawn jump
                self.lastPawnJump = (end1, end2
                                     )  # Stores the pawn if it was a jump
                self.turnAddedPassant = 0
                board[end1][end2] = board[start1][
                    start2]  # Changes the end square to contain the piece
                board[start1][
                    start2] = None  # Changes previous square to nothing
                board[end1][end2].x, board[end1][end2].y = end2, end1
                board[end1][end2].moveCount += 1  # Adds one to the move count
            else:  # Normal move without storing if it wasn't a jump
                try:
                    if realgame:
                        board[end1][end2].alive = False
                except:
                    pass
                board[end1][end2] = board[start1][
                    start2]  # Changes the end square to contain the piece
                board[start1][
                    start2] = None  # Changes previous square to nothing
                board[end1][end2].x, board[end1][end2].y = end2, end1
                board[end1][end2].moveCount += 1  # Adds one to the move count

        elif isinstance(board[start1][start2], King) and abs(start2 - end2) == 2:
            if (start2 - end2) == -2:
                board[end1][end2] = board[start1][
                    start2]  # Changes the end square to contain the piece
                board[start1][
                    start2] = None  # Changes previous square to nothing
                board[end1][end2].x, board[end1][end2].y = end2, end1
                board[end1][end2].moveCount += 1  # Adds one to the move count

                board[end1][end2 - 1] = board[start1][start2 + 3]  # Moving the rook for castling
                board[start1][start2 + 3] = None
                board[end1][end2 - 1].x, board[end1][end2 - 1].y = end2 - 1, end1

            if (start2 - end2) == 2:
                board[end1][end2] = board[start1][
                    start2]  # Changes the end square to contain the piece
                board[start1][
                    start2] = None  # Changes previous square to nothing
                board[end1][end2].x, board[end1][end2].y = end2, end1
                board[end1][end2].moveCount += 1  # Adds one to the move count

                board[end1][end2 + 1] = board[start1][start2 - 4]  # Moving the rook for castling
                board[start1][start2 - 4] = None
                board[end1][end2 + 1].x, board[end1][end2 + 1].y = end2 + 1, end1


        else:
            try:
                if realgame:
                    board[end1][end2].alive = False
            except:
                pass
            board[end1][end2] = board[start1][
                start2]  # Changes the end square to contain the piece
            board[start1][start2] = None  # Changes previous square to nothing
            board[end1][end2].x, board[end1][end2].y = end2, end1
            board[end1][end2].moveCount += 1  # Adds one to the move count
        # print("Moved. (Debugging purposes DO NOT LEAVE IN FINAL PRODUCT)")

    def resetgrid(
            self):  # Loops through the board and essentially just makes sure the colour of each square is default
        for z in range(8):
            for q in range(8):
                if (z + q) % 2 == 0:
                    self.grid[z][q].colour = lbrown
                else:
                    self.grid[z][q].colour = dbrown

    def resetboard(self, board):
        for z in range(8):
            for q in range(8):
                if board[z][
                    q] == 'x':  # These if statements check for possible moves and removes them.
                    board[z][q] = None
                elif board[z][q] == None:
                    pass
                else:
                    board[z][q].killable = False

    def fullreset(self, board):
        self.resetboard(board)
        self.resetgrid()

    def checkPawn(self):
        pos = (None, None)
        for z in range(8):  # Checks if there are any pawns in the final rows.
            if str(
                    type(self.board[0][z])
            ) == "<class 'pieces.Pawn'>":  # Checks whether the piece is or isn't a pawn.
                self.promotion = True  # Initiates pawn change function
                pos = (z, 0)  # Returns pos of pawn
                break
            elif str(
                    type(self.board[7][z])
            ) == "<class 'pieces.Pawn'>":  # Checks whether the piece is or isn't a pawn.
                self.promotion = True  # Initiates pawn change function
                pos = (z, 0)  # Returns pos of pawn
                break

        return pos

    def pawnChange(self, choice, pos):
        y, x = pos[1], pos[0]
        if self.board[y][x].team == "black":
            if choice == "Queen":
                name = Queen(
                    "white", "bQ.png", self.board[y]
                    [x].rect)  # Creates a new class for the new queen.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Rook":
                name = Rook("white", "bR.png", self.board[y]
                [x].rect)  # Creates a new class for the new rook.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Horse":
                name = Horse(
                    "white", "bH.png", self.board[y]
                    [x].rect)  # Creates a new class for the new horse.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Bishop":
                name = Bishop(
                    "white", "bB.png", self.board[y]
                    [x].rect)  # Creates a new class for the new bishop.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

        elif self.board[y][x].team == "white":
            if choice == "Queen":
                name = Queen(
                    "white", "wQ.png", self.board[y]
                    [x].rect)  # Creates a new class for the new queen.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Rook":
                name = Rook("white", "wR.png", self.board[y]
                [x].rect)  # Creates a new class for the new rook.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Horse":
                name = Horse(
                    "white", "wH.png", self.board[y]
                    [x].rect)  # Creates a new class for the new horse.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

            elif choice == "Bishop":
                name = Bishop(
                    "white", "wB.png", self.board[y]
                    [x].rect)  # Creates a new class for the new bishop.
                name.y, name.x = y, x  # Uses old position
                name.moveCount = self.board[y][
                    x].moveCount  # Movecount for stats sake
                self.board[y][x] = name
                self.promotion = False

    def menuPawnPromote(self, screen):
        pos = self.checkPawn()
        menu = pygame_menu.Menu('Pawn  Promotion',
                                400,
                                300,
                                theme=pygame_menu.themes.THEME_BLUE)

        menu.add.button('Bishop', self.pawnChange, "Bishop", pos)
        menu.add.button('Rook', self.pawnChange, "Rook", pos)
        menu.add.button('Horse', self.pawnChange, "Horse", pos)
        menu.add.button('Queen', self.pawnChange, "Queen", pos)
        menu.add.button('Confirm', menu.disable)

        menu.mainloop(screen)

    def moveEnPassant(self, startpos, enpassantpos, board):
        start2, start1 = startpos
        enp1, enp2 = enpassantpos

        if board[start1][start2].team == "white":
            board[enp1][enp2].alive = False
            board[enp1][enp2] = None  # Kills the EnPassant Pawn
            board[enp1 - 1][enp2] = board[start1][
                start2]  # Moves the correct piece to the correct location
            board[start1][start2] = None  # Changes previous square to nothing
            board[enp1 - 1][enp2].moveCount += 1  # Adds one to the move count
        else:
            board[enp1][enp2].alive = False
            board[enp1][enp2] = None  # Kills the EnPassant Pawn
            board[enp1 + 1][enp2] = board[start1][
                start2]  # Moves the correct piece to the correct location
            board[start1][start2] = None  # Changes previous square to nothing
            board[enp1 + 1][enp2].moveCount += 1  # Adds one to the move count 

    def enPassantCheck(self):
        if self.lastPawnJump is not None:  # Checker to see if en passant is still viable
            if self.turnAddedPassant == 0:
                self.turnAddedPassant += 1  # Adds one to the turn counter so it will reset next turn
            else:  # If not reset it
                self.turnAddedPassant = 0
                self.lastPawnJump = None

    def kingTracker(self):
        return (bK1.y, bK1.x), (wK1.y, wK1.x)

    def checkChecker(self, board, team):
        # print(bK1.y, bK1.x, wK1.y, wK1.x, "BKing Pos and WKing Pos")
        check = False
        if team == "black":
            wlegalAttacks = board[wK1.y][wK1.x].legalAttacks(
                board)
            # print(wlegalAttacks, "Legal Attackers on King")
            for pieces in wlegalAttacks:
                temp = board[pieces[0]][pieces[1]].possible(board)
                for pos in temp:
                    if pos == (wK1.y, wK1.x):
                        self.attackers.append(board[pos[0]][pos[1]])
                        check = True
            if check:
                return True
            else:
                self.attackers = []
                return False

        else:
            blegalAttacks = board[bK1.y][bK1.x].legalAttacks(
                board)
            # print(blegalAttacks, "Legal attackers on black king")
            for pieces in blegalAttacks:
                temp = board[pieces[0]][pieces[1]].possible(board)
                for pos in temp:
                    if pos == (bK1.y, bK1.x):
                        self.attackers.append(board[pos[0]][pos[1]])
                        check = True
            if check:
                return True
            else:
                self.attackers = []
                return False

    def checkmateChecker(self, screen):
        self.checkmate = True
        allposmoves = [[] for _ in range(16)]
        if self.turn % 2 == 0:
            for i in range(16):
                if whiteTeam[i].alive:
                    posmoves = self.posMoves(whiteTeam[i], self.board)
                    for move in posmoves:
                        self.ghostSave()
                        copyboard = [list(self.board[x]) for x in range(8)]
                        self.fullreset(copyboard)
                        self.posmovesApply(whiteTeam[i], posmoves, copyboard)
                        self.move((whiteTeam[i].x, whiteTeam[i].y), move, copyboard, False)
                        if self.checkChecker(copyboard, "black"):
                            pass
                        else:
                            allposmoves[i].append(move)
                            self.checkmate = False
                        self.ghostReset()
        else:
            for i in range(16):
                if blackTeam[i].alive:
                    posmoves = self.posMoves(blackTeam[i], self.board)
                    for move in posmoves:
                        self.ghostSave()
                        copyboard = [list(self.board[x]) for x in range(8)]
                        self.fullreset(copyboard)
                        self.posmovesApply(blackTeam[i], posmoves, copyboard)
                        self.move((blackTeam[i].x, blackTeam[i].y), move, copyboard, False)
                        if self.checkChecker(copyboard, "white"):
                            pass
                        else:
                            allposmoves[i].append(move)
                            self.checkmate = False
                        self.ghostReset()

        if self.checkmate:
            return self.checkmate
        else:
            print(allposmoves, "ALL POSSIBLE MOVES IN CHECK")
            return allposmoves

    def gameStart(self):
        while self.winner == None:
            b.openg()
        return self.winner

    def opengC(self):
        pygame.init()  # Initialise pygame
        self.screen = pygame.display.set_mode([800, 800])
        grid = self.creategrid()
        picked = False  # Is there a piece picked?
        selected = (0, 0)  # Which piece is picked
        CHECK = pygame.event.custom_type()
        CHECKMATE = pygame.event.custom_type()
        BOT = pygame.event.custom_type()

        running = True
        while running:  # While loop to close game when user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # User clicking the close button
                    running = False

                if event.type == BOT:
                    x = stockfish.get_best_move()
                    temp = Fen.myMoves(self, x)
                    print(temp)

                    self.move(
                        temp[0],
                        temp[1], self.board, True)  # Moves the piece accordingly
                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                    self.enPassantCheck()
                    self.kingTracker()
                    self.check = self.checkChecker(self.board, "black")
                    self.fullreset(self.board)
                    self.checkPawn()
                    pygame.event.post(pygame.event.Event(CHECK))
                    stockfish.make_moves_from_current_position([x])
                    print("Bot move done")  # DEBUG

                if event.type == CHECK:
                    if self.checkmate:
                        break

                    print("CHECK: ", self.check)
                    if self.check:
                        allpossible = None
                        if self.turn % 2 == 0:  # Checks if its the correct turn
                            allpossible = self.checkmateChecker(self.screen)
                        elif self.turn % 2 == 1:  # Checks if its the correct turn
                            allpossible = self.checkmateChecker(self.screen)

                    if self.promotion:
                        self.menuPawnPromote(self.screen)
                        pygame.event.post(pygame.event.Event(CHECK))

                    self.fullreset(self.board)


                elif event.type == pygame.MOUSEBUTTONDOWN:  # User clicking anywhere on the game window
                    pos = pygame.mouse.get_pos(
                    )  # Gets the coordinates of the mouse
                    x, y = self.locatesquare(
                        pos
                    )  # Saves the coordinates of the square the mouse selected
                    # print(x, y)  # Testing Purposes

                    if not self.check:
                        if not picked:
                            if self.board[y][x] is not None:
                                if self.turn % 2 == 0 and self.board[y][
                                    x].team == "white":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        possible = self.posMoves(
                                            self.board[y][x], self.board)
                                        self.posmovesApply(self.board[y][x], possible, self.board)
                                        # Saves possible moves to an array
                                        self.visible(
                                            possible
                                        )  # Makes the pieces visible for possible moves

                                    finally:
                                        pass
                                else:
                                    print(
                                        "It is not your turn (Debugging purposes, DO NOT LEAVE AS FINAL PRODUCT)"
                                    )

                        elif self.board[y][
                            x] is not None:  # Checks not none as all possible moves are marked.
                            try:
                                if self.board[y][
                                    x].killable:  # This is for when a piece occupies the space
                                    self.move(
                                        selected,
                                        (y, x), self.board, True)  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    pygame.event.post(pygame.event.Event(BOT))
                                    stockfish.make_moves_from_current_position([Fen.revMyMoves(self, selected, (y, x))])
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

                            except AttributeError:
                                if self.board[y][
                                    x] == 'x':  # This is for when its an empty space
                                    if self.lastPawnJump != None:
                                        if x != selected[0] and y == selected[1]:
                                            if isinstance(self.board[selected[1]][selected[0]], Pawn):
                                                self.moveEnPassant(selected, self.lastPawnJump, self.board)

                                                # Runs en passant if check completes.
                                        else:
                                            self.move(
                                                selected, (y, x), self.board, True
                                            )  # Moves the piece accordingly
                                    else:
                                        self.move(selected, (y, x), self.board, True
                                                  )  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    pygame.event.post(pygame.event.Event(BOT))
                                    stockfish.make_moves_from_current_position([Fen.revMyMoves(self, selected, (y, x))])
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False
                    if self.check:
                        if not picked:
                            if self.board[y][x] is not None:
                                if self.turn % 2 == 0 and self.board[y][
                                    x].team == "white":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        print(self.posMoves(self.board[y][x], self.board))
                                        self.posmovesApply(self.board[y][x], allpossible[whiteTeam[self.board[y][x]]],
                                                           self.board)
                                        self.visible(allpossible[whiteTeam[self.board[y][x]]])
                                        # Makes the pieces visible for possible moves

                                    finally:
                                        pass

                                else:
                                    print(
                                        "It is not your turn (Debugging purposes, DO NOT LEAVE AS FINAL PRODUCT)"
                                    )

                        elif self.board[y][
                            x] is not None:  # Checks not none as all possible moves are marked.
                            try:
                                if self.board[y][
                                    x].killable:  # This is for when a piece occupies the space
                                    self.move(
                                        selected,
                                        (y, x), self.board, True)  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    pygame.event.post(pygame.event.Event(BOT))
                                    stockfish.make_moves_from_current_position([Fen.revMyMoves(self, selected, (y, x))])
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

                            except AttributeError:
                                if self.board[y][
                                    x] == 'x':  # This is for when its an empty space
                                    if self.lastPawnJump != None:
                                        if x != selected[0] and y == selected[1]:
                                            if isinstance(self.board[selected[1]][selected[0]], Pawn):
                                                self.moveEnPassant(selected, self.lastPawnJump, self.board)

                                                # Runs en passant if check completes.
                                        else:
                                            self.move(
                                                selected, (y, x), self.board, True
                                            )  # Moves the piece accordingly
                                    else:
                                        self.move(selected, (y, x), self.board, True
                                                  )  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    pygame.event.post(pygame.event.Event(BOT))
                                    stockfish.make_moves_from_current_position([Fen.revMyMoves(self, selected, (y, x))])
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

            if self.checkmate:
                break
            self.refresh(grid)
        if self.turn % 2 == 0:
            return "black"
        else:
            return "white"

    def openg(self):
        pygame.init()  # Initialise pygame
        self.screen = pygame.display.set_mode([800, 800])
        grid = self.creategrid()
        picked = False  # Is there a piece picked?
        selected = (0, 0)  # Which piece is picked
        CHECK = pygame.event.custom_type()
        CHECKMATE = pygame.event.custom_type()

        running = True
        while running:  # While loop to close game when user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # User clicking the close button
                    running = False

                if event.type == CHECK:
                    if self.checkmate:
                        break

                    print("CHECK: ", self.check)
                    if self.check:
                        allpossible = None
                        if self.turn % 2 == 0:  # Checks if its the correct turn
                            allpossible = self.checkmateChecker(self.screen)
                        elif self.turn % 2 == 1:  # Checks if its the correct turn
                            allpossible = self.checkmateChecker(self.screen)

                    if self.promotion:
                        self.menuPawnPromote(self.screen)
                        pygame.event.post(pygame.event.Event(CHECK))

                    self.fullreset(self.board)


                elif event.type == pygame.MOUSEBUTTONDOWN:  # User clicking anywhere on the game window
                    pos = pygame.mouse.get_pos(
                    )  # Gets the coordinates of the mouse
                    x, y = self.locatesquare(
                        pos
                    )  # Saves the coordinates of the square the mouse selected
                    # print(x, y)  # Testing Purposes

                    if not self.check:
                        if not picked:
                            if self.board[y][x] is not None:
                                if self.turn % 2 == 0 and self.board[y][
                                    x].team == "white":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        possible = self.posMoves(
                                            self.board[y][x], self.board)
                                        self.posmovesApply(self.board[y][x], possible, self.board)
                                        # Saves possible moves to an array
                                        self.visible(
                                            possible
                                        )  # Makes the pieces visible for possible moves

                                    finally:
                                        pass

                                elif self.turn % 2 == 1 and self.board[y][
                                    x].team == "black":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        possible = self.posMoves(
                                            self.board[y][x], self.board)
                                        self.posmovesApply(self.board[y][x], possible, self.board)
                                        # Saves possible moves to an array
                                        self.visible(
                                            possible
                                        )  # Makes the pieces visible for possible moves

                                    finally:
                                        pass

                                else:
                                    print(
                                        "It is not your turn (Debugging purposes, DO NOT LEAVE AS FINAL PRODUCT)"
                                    )

                        elif self.board[y][
                            x] is not None:  # Checks not none as all possible moves are marked.
                            try:
                                if self.board[y][
                                    x].killable:  # This is for when a piece occupies the space
                                    self.move(
                                        selected,
                                        (y, x), self.board, True)  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

                            except AttributeError:
                                if self.board[y][
                                    x] == 'x':  # This is for when its an empty space
                                    if self.lastPawnJump != None:
                                        if x != selected[0] and y == selected[1]:
                                            if isinstance(self.board[selected[1]][selected[0]], Pawn):
                                                self.moveEnPassant(selected, self.lastPawnJump, self.board)

                                                # Runs en passant if check completes.
                                        else:
                                            self.move(
                                                selected, (y, x), self.board, True
                                            )  # Moves the piece accordingly
                                    else:
                                        self.move(selected, (y, x), self.board, True
                                                  )  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False
                    if self.check:
                        if not picked:
                            if self.board[y][x] is not None:
                                if self.turn % 2 == 0 and self.board[y][
                                    x].team == "white":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        print(self.posMoves(self.board[y][x], self.board))
                                        self.posmovesApply(self.board[y][x], allpossible[whiteTeam[self.board[y][x]]],
                                                           self.board)
                                        self.visible(allpossible[whiteTeam[self.board[y][x]]])
                                        # Makes the pieces visible for possible moves

                                    finally:
                                        pass

                                elif self.turn % 2 == 1 and self.board[y][
                                    x].team == "black":  # Checks if its the correct turn
                                    try:
                                        self.grid[y][
                                            x].colour = lblue  # Visually represents selected square
                                        selected = (
                                            x, y
                                        )  # Changes selected square to this
                                        picked = True  # Updates picked value
                                        self.posmovesApply(self.board[y][x], allpossible[blackTeam[self.board[y][x]]],
                                                           self.board)
                                        self.visible(
                                            allpossible[blackTeam[self.board[y][x]]]
                                        )  # Makes the pieces visible for possible moves

                                    finally:
                                        pass

                                else:
                                    print(
                                        "It is not your turn (Debugging purposes, DO NOT LEAVE AS FINAL PRODUCT)"
                                    )

                        elif self.board[y][
                            x] is not None:  # Checks not none as all possible moves are marked.
                            try:
                                if self.board[y][
                                    x].killable:  # This is for when a piece occupies the space
                                    self.move(
                                        selected,
                                        (y, x), self.board, True)  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

                            except AttributeError:
                                if self.board[y][
                                    x] == 'x':  # This is for when its an empty space
                                    if self.lastPawnJump != None:
                                        if x != selected[0] and y == selected[1]:
                                            if isinstance(self.board[selected[1]][selected[0]], Pawn):
                                                self.moveEnPassant(selected, self.lastPawnJump, self.board)

                                                # Runs en passant if check completes.
                                        else:
                                            self.move(
                                                selected, (y, x), self.board, True
                                            )  # Moves the piece accordingly
                                    else:
                                        self.move(selected, (y, x), self.board, True
                                                  )  # Moves the piece accordingly
                                    self.turn += 1  # Adds one to the turn so it can check who's turn it is
                                    self.enPassantCheck()
                                    self.kingTracker()
                                    self.check = self.checkChecker(self.board, self.board[y][x].team)
                                    self.fullreset(self.board)
                                    self.checkPawn()
                                    pygame.event.post(pygame.event.Event(CHECK))
                                    picked = False

                                else:
                                    self.fullreset(self.board)
                                    picked = False

            if self.checkmate:
                break
            self.refresh(grid)
        if self.turn % 2 == 0:
            return "black"
        else:
            return "white"

b = Board()
