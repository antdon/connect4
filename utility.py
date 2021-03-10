from board import *
from typing import List, Set, Dict, Tuple, Optional

class Utility:
    def __init__(self, board):
        self.board = board

    def check_full(self, xInd):
        board = self.board 
        if board[0][column] == '-':
            return False
        else:
            return True

    def check_if_edge(self, insY: int, insX: int) -> List[str]:
        edgeCollisions = []
        if insY == 0:
            edgeCollisions.append('N')
        elif insY == self.board.get_length() - 1:
            edgeCollisions.append('S')
        if insX == 0:
            edgeCollisions.append('E')
        elif insX == self.board.get_width() - 1:
            edgeCollisions.append('W')

        return edgeCollisions

    def check_potential_win_directions(self, insY: int, insX: int, dontCheck: List[str], team: str) -> List[str]:
        potentialDirections = []
        if not 'W' in dontCheck and self.board.get_square(insY, insX - 1) == team:
            potentialDirections.append('W')
        if not 'E' in dontCheck and self.board.get_square(insY, insX + 1) == team:
            potentialDirections.append('E')
        if not 'N' in dontCheck and self.board.get_square(insY - 1, insX) == team:
            potentialDirections.append('N')
        if not 'S' in dontCheck and self.board.get_square(insY + 1, insX) == team:
            potentialDirections.append('S')
        if not 'N' in dontCheck and not 'E' in dontCheck and self.board.get_square(insY - 1, insX + 1) == team:
            potentialDirections.append('NE')
        if not 'S' in dontCheck and not 'E' in dontCheck and self.board.get_square(insY + 1, insX + 1) == team:
            potentialDirections.append('SE')
        if not 'S' in dontCheck and not 'W' in dontCheck and self.board.get_square(insY + 1, insX - 1) == team:
            potentialDirections.append('SW')
        if not 'N' in dontCheck and not 'W' in dontCheck and self.board.get_square(insY - 1, insX - 1) == team:
            potentialDirections.append('NW')
        return potentialDirections


