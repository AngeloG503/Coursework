import pygame


class Piece:  # Base piece class, used for inheritance
    def __init__(self, team, image, rect):
        self.sprite = pygame.sprite.Sprite()  # Sprite used for the piece
        self.image = pygame.image.load(image)  # For sprites on the visual board
        self.team = team  # Whether a piece is on black or white team
        self.killable = False  # Whether a piece can be killed or not
        self.moveCount = 0  # For special moves, e.g en passant
        self.x, self.y = 0, 0  # In terms of the grid array
        self.pos = (self.y, self.x)
        self.rect = pygame.Rect(rect)  # For drawing purposes in pygame

    def onboard(self, x, y):  # Checks whether position is on the board
        if -1 < x < 8:
            if -1 < y < 8:
                return True
            else:
                return False
        else:
            return False

    def possiblechecker(self, posarray, board):  # Function that checks whether a piece is a real possible move and
        # whether it is a free space or a piece is there, and decides whether it is killable or not.
        possiblemoves = []  # Array to store all the real possible moves.
        for attempt in posarray:
            for pos in attempt:
                if self.onboard(pos[0], pos[1]):  # Checks if the position is on the board or not.
                    if board[pos[0]][pos[1]] is None:  # Checks if the space is empty.
                        possiblemoves.append((pos[0], pos[1]))  # Adds it to the possible moves array.
                    else:
                        if board[pos[0]][pos[1]] is not 'x':
                            if board[pos[0]][pos[1]].team is not self.team:  # Checks if piece is opposite team
                                board[pos[0]][pos[1]].killable = True  # If it is then it is killable.
                                possiblemoves.append((pos[0], pos[1]))  # Adds it to the possible moves array.
                                break
                            else:
                                break
                else:
                    break
        return possiblemoves

class Pawn(Piece):
    def possible(self, board):
        possiblemoves = []
        if self.team == "black":
            try:
                if board[self.y + 2][self.x] is None and self.moveCount == 0:
                    possiblemoves.append((self.y + 2, self.x))

                if board[self.y + 1][self.x] is None:
                    possiblemoves.append((self.y + 1, self.x))

                if self.onboard((self.x + 1), (self.y + 1)):
                    if board[self.y + 1][self.x + 1] is not None:
                        if board[self.y + 1][self.x + 1] is not 'x':
                            if board[self.y + 1][self.x + 1].team is not self.team:
                                board[self.y + 1][self.x + 1].killable = True
                                possiblemoves.append((self.y + 1, self.x + 1))

                if self.onboard((self.x - 1), (self.y + 1)):
                    if board[self.y + 1][self.x - 1] is not None:
                        if board[self.y + 1][self.x - 1] is not 'x':
                          if board[self.y + 1][self.x - 1].team is not self.team:
                                board[self.y + 1][self.x - 1].killable = True
                                possiblemoves.append((self.y + 1, self.x - 1))

                if self.y + 1 > 7:
                    pass
            finally:
                pass

        else:
            try:
                if board[self.y - 2][self.x] is None and self.moveCount == 0:
                    possiblemoves.append((self.y - 2, self.x))

                if board[self.y - 1][self.x] is None:
                    possiblemoves.append((self.y - 1, self.x))

                if self.onboard((self.x + 1), (self.y - 1)):
                    if board[self.y - 1][self.x + 1] is not None:
                        if board[self.y - 1][self.x + 1] is not 'x':
                            if board[self.y - 1][self.x + 1].team is not self.team:
                                board[self.y - 1][self.x + 1].killable = True
                                possiblemoves.append((self.y - 1, self.x + 1))

                if self.onboard((self.x - 1), (self.y - 1)):
                    if board[self.y - 1][self.x - 1] is not None:
                        if board[self.y - 1][self.x - 1] is not 'x':
                            if board[self.y - 1][self.x - 1].team is not self.team:
                                board[self.y - 1][self.x - 1].killable = True
                                possiblemoves.append((self.y - 1, self.x - 1))

                if self.y - 1 < 0:
                    pass
            finally:
                pass
        return possiblemoves


class Rook(Piece):
    def possible(self, board):
        straight = [[[self.y, self.x + z] for z in range(1, 8)],  # This array holds all the possible moves for a
                    [[self.y + z, self.x] for z in range(1, 8)],  # rook going 8 in every straight direction.
                    [[self.y - z, self.x] for z in range(1, 8)],
                    [[self.y, self.x - z] for z in range(1, 8)]
                    ]

        return self.possiblechecker(straight, board)  # Returns the possible moves array after checking the moves.


class Bishop(Piece):
    def possible(self, board):
        diagonal = [[[self.y + z, self.x + z] for z in range(1, 8)],  # This array holds all the possible moves for a
                    [[self.y + z, self.x - z] for z in range(1, 8)],  # bishop going 8 diagonally in every direction.
                    [[self.y - z, self.x + z] for z in range(1, 8)],
                    [[self.y - z, self.x - z] for z in range(1, 8)]
                    ]

        return self.possiblechecker(diagonal, board)  # Returns the possible moves array after checking the moves.

class Horse(Piece):
    def possible(self, board):
        pythag = []  # Since the formula technically requires pythagoras theorem, this is the variable name.
        for z in range(-2, 3):  # Starts from a negative number that makes it so I can build a 5x5 grid around the piece
            for q in range(-2, 3):
                if (z * z) + (q * q) == 5:  # Using pythagoras theorem, I can determine the attempted possible moves.
                    pythag.append([[self.y + z, self.x + q]])  # Adds it to the array.

        return self.possiblechecker(pythag, board)

class King(Piece):
    def possible(self, board):
        onespace = []  # array for one space around it.
        for z in range(-1, 2):  # Starts from a negative number that makes it so I can build a 1x1 grid around the piece
            for q in range(-1, 2):
                onespace.append([[self.y + z, self.x + q]])  # Adds it to the array.

        return self.possiblechecker(onespace, board)

    def legalAttacks(self, board):  # Function that checks whether a piece is a real possible move and
        # whether it is a free space or a piece is there, and decides whether it is killable or not.

        everywhere = [[[self.y, self.x + z] for z in range(1, 8)],
                      [[self.y + z, self.x] for z in range(1, 8)],  # This array holds all the possible positions for anything in a direct diagonal or straight line from the King
                      [[self.y - z, self.x] for z in range(1, 8)],
                      [[self.y, self.x - z] for z in range(1, 8)],
                      [[self.y + z, self.x + z] for z in range(1, 8)],
                      [[self.y + z, self.x - z] for z in range(1, 8)],
                      [[self.y - z, self.x + z] for z in range(1, 8)],
                      [[self.y - z, self.x - z] for z in range(1, 8)]
                      ]

        possibleattack = []  # Array to store all the real possible moves.

        for attempt in everywhere:
            for pos in attempt:
                if self.onboard(pos[0], pos[1]):  # Checks if the position is on the board or not.
                    if board[pos[0]][pos[1]] is not None:  # Checks if the space is empty.
                        if board[pos[0]][pos[1]] is not 'x':
                            if board[pos[0]][pos[1]].team is not self.team:
                                possibleattack.append((pos[0], pos[1]))  # Adds it to the possible moves array.

        return possibleattack


class Queen(Piece):
    def possible(self, board):
        everywhere = [[[self.y, self.x + z] for z in range(1, 8)],  # This array holds all the possible moves for a
                     [[self.y + z, self.x] for z in range(1, 8)],   # queen going 8 in every direction.
                     [[self.y - z, self.x] for z in range(1, 8)],
                     [[self.y, self.x - z] for z in range(1, 8)],
                     [[self.y + z, self.x + z] for z in range(1, 8)],
                     [[self.y + z, self.x - z] for z in range(1, 8)],
                     [[self.y - z, self.x + z] for z in range(1, 8)],
                     [[self.y - z, self.x - z] for z in range(1, 8)]
        ]

        return self.possiblechecker(everywhere, board)