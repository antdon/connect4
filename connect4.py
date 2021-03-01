import pdb

class Board:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.board = [['-' for i in range(self.width)] for j in range(self.length)]
    def printBoard(self):
        for ind, spots in enumerate(self.board):
            for spot in spots:
                print(spot, end = " ")
            print("\n")
        for ind, column in enumerate(range(self.width)):
            print(chr(ind + ord('A')), end = " ")
            
                    
b = Board(6,10)
b.printBoard()

