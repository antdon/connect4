from board import *
from typing import List, Set, Dict, Tuple, Optional

class Utility:
    def __init__(self, board):
        self.board = board

    def check_full(self, column):
        board = self.board 
        if board[0][column] == '-':
            return False
        else:
            return True

    def check_if_edge(self, insRow: int, insCol: int) -> List[str]:
        edgeCollisions = []
        if insRow == 0:
            edgeCollisions.append('N')
        elif insRow == self.board.get_length():
            edgeCollisions.append('S')
        if insCol == 0:
            edgeCollisions.append('E')
        elif insCol == self.board.get_width():
            edgeCollisions.append('W')

        return edgeCollisions

#   def check_win_directions(self, insRow, insCol):
#       NisEdge = False
#       potentialDirections = []
#       team = board[insRow][insCol]
#       if insRow == self.get_width() or insCol == self.get_length:
#           isEdge = True
#       if board[insRow][insCol - 1] == team:
#           potentialDirections.append('W')
#       if board[insRow][insCol + 1] == team:
#           potentialDirections.append('E')
#       if board[insRow + 1][insCol] == team:
#           potentialDirections.append('N')
#       if board[insRow - 1][insCol] == team:
#           potentialDirections.append('S')
#       if board[insRow + 1][insCol + 1] == team:
#           potentialDirections.append('NE')
#       if board[insRow - 1][insCol + 1] == team:
#           potentialDirections.append('SE')
#       if board[insRow - 1][insCol - 1] == team:
#           potentialDirections.append('SW')
#       if board[insRow + 1][insCol - 1] == team:
#           potentialDirections.append('NW')


