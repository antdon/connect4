import pdb

class Board:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.board = [['-' for i in range(self.width)] for j in range(self.length)]

    def insert_piece(self, team: str, xInd):
        insertionY = -1
        insertionX = -1
        for yInd in range(self.length):
            if self.get_square(yInd, xInd) == '-':
                insertionY = yInd
                insertionX = xInd
        if insertionY == -1 and insertionX == -1:
           return []
        self.set_square(insertionY, insertionX, team)
        return [insertionY, insertionX]

    def get_board(self):
        return self.board

    def get_length(self):
        return self.length #note that this is +1 on the index  

    def get_width(self):
        return self.width

    def get_square(self, yInd, xInd):
        return self.board[yInd][xInd]

    def set_square(self, yInd, xInd, value: str):
        self.board[yInd][xInd] = value

    def print_board(self):
        for ind, spots in enumerate(self.get_board()):
            for spot in spots:
                print(spot, end = " ")
            print("\n")
        for xInd in range(self.width):
            print(chr(xInd + ord('A')), end = " ")
                    

