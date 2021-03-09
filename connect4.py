from board import *
from utility import *

class Play:
    def __init__(self):
        self.board = Board(5,5)
        self.utilities = Utility(self.board)

    def play(self):
        [insertionRow, insertionCol] = self.board.insert_piece('X', 3)
        length = self.board.get_length()
        print(length)
        print(self.utilities.check_if_edge(insertionRow+1, insertionCol))
        self.board.print_board()


p = Play()
p.play()
