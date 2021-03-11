from board import *
from utility import *
import pdb

class Play:
    def __init__(self):
        self.board = Board(5,5)
        self.utilities = Utility(self.board)

    def play(self):
        [insertionY, insertionX] = self.board.insert_piece('X', 3)
        nearEdges = self.utilities.check_if_edge(insertionY, insertionX)
        self.utilities.check_potential_win_directions(insertionY, insertionX, nearEdges, 'X')
        self.board.insert_piece('X', 3)
        nearEdges = self.utilities.check_if_edge(insertionY, insertionX)
        print(self.board.get_length() - 1)
        print(nearEdges)
        print(self.utilities.check_potential_win_directions(insertionY, insertionX, nearEdges, 'X'))
        self.board.insert_piece('X', 3)
        nearEdges = self.utilities.check_if_edge(insertionY, insertionX)
        self.utilities.check_potential_win_directions(insertionY, insertionX, nearEdges, 'X')
        print(insertionY)
        self.board.insert_piece('X', 3)
        nearEdges = self.utilities.check_if_edge(insertionY, insertionX)
        self.utilities.check_potential_win_directions(insertionY, insertionX, nearEdges, 'X')
        print(insertionY)
        self.board.insert_piece('X', 3)
        nearEdges = self.utilities.check_if_edge(insertionY, insertionX)
        self.utilities.check_potential_win_directions(insertionY, insertionX, nearEdges, 'X')
        print(insertionY)
        print('')
        print(self.utilities.check_North(insertionY, insertionX, 'X'))
        self.board.print_board()


p = Play()
p.play()
