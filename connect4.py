import pdb

class Board:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.board = [['-' for i in range(self.width)] for j in range(self.length)]
    def insert_piece(self, team, column):
        insertionRow = -1
        insertionColumn = -1
        for row in range(self.length):
            if self.get_square(row, column) == '-':
                insertionRow = row
                insertionColumn = column
        if insertionRow == -1 and insertionColumn == -1:
           return 0
        self.set_square(insertionRow, insertionColumn, team)
        return 1
                



    def get_board(self):
        return self.board

    def get_square(self, length, width):
        return self.board[length][width]

    def set_square(self, length, width, value):
        self.board[length][width] = value

    def print_board(self):
        for ind, spots in enumerate(self.get_board()):
            for spot in spots:
                print(spot, end = " ")
            print("\n")
        for column in range(self.width):
            print(chr(column + ord('A')), end = " ")
            
                    
b = Board(6,10)
b.insert_piece('X', 4)
b.insert_piece('X', 4)
b.insert_piece('X', 4)
b.insert_piece('X', 3)
b.print_board()

