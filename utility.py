from board import *
from typing import List, Set, Dict, Tuple, Optional

class Utility:
    def __init__(self, board: List[List]) -> None:
        self.board: Board = board

    def check_full(self, xInd: int) -> None:
        if self.board[0][xInd] == '-':
            return False
        else:
            return True

    def check_if_edge(self, insY: int, insX: int) -> List[str]:
        edgeCollisions: List[str] = []
        if insY == 0:
            edgeCollisions.append('N')
        elif insY == self.board.get_length() - 1:
            edgeCollisions.append('S')
        if insX == 0:
            edgeCollisions.append('W')
        elif insX == self.board.get_width() - 1:
            edgeCollisions.append('E')

        return edgeCollisions
    
    def check_win(self, insY: int, insX: int, team: str) -> bool:
        dontCheck: List[str] = self.check_if_edge(insY, insX)
        potentialDirections: List[str] = self.check_potential_win_directions(insY, insX, dontCheck, team)
        for direction in potentialDirections:
            if direction == 'N' and self.check_north(insY, insX, team):
                return True
            elif direction == 'S' and self.check_south(insY,  insX, team):
                return True
            elif direction == 'E' and self.check_east(insY,  insX, team):
                return True
            elif direction == 'W' and self.check_west(insY,  insX, team):
                return True
            elif direction == 'NE' and self.check_north_east(insY,  insX, team):
                return True
            elif direction == 'NW' and self.check_north_west(insY,  insX, team):
                return True
            elif direction == 'SE' and self.check_south_east(insY,  insX, team):
                return True
            elif direction == 'SW' and self.check_south_west(insY,  insX, team):
                return True
        return False


    def check_potential_win_directions(self, insY: int, insX: int, dontCheck: List[str], team: str) -> List[str]:
        potentialDirections: List[str] = []
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

    def check_north(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insY
        for ind in range(3):
            tmp -= 1
            if tmp == 0:
                return False
            if self.board.get_square(tmp, insX) != team:
                return False
        return True

    def check_south(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insY
        for ind in range(3):
            tmp += 1
            if tmp == self.board.get_length():
                return False
            if self.board.get_square(tmp, insX) != team:
                return False
        return True

    #check_east backchecks for the horizontal line
    def check_east(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        atEnd: bool = False
        count: int = 0
        for ind in range(3):
            tmp += 1
            if tmp == self.board.get_width():
                atEnd = True
                break
            if self.board.get_square(insY, tmp) != team:
                atEnd = True
                break
            else:
                count += 1
        if atEnd:
            tmp = insX 
            for ind in range(3-count):
                tmp -= 1
                if tmp == 0:
                    return False
                if self.board.get_square(insY, tmp) != team:
                    return False
        return True

    def check_west(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        for ind in range(3):
            tmp -= 1
            if tmp == 0:
                return False
            if self.board.get_square(insY, tmp) != team:
                return False
        return True

    def check_north_east(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        tmp2: int = insY
        for ind in range(3):
            tmp += 1
            tmp2 -= 1
            if tmp2 == 0 or tmp == self.board.get_width():
                return False
            if self.board.get_square(tmp2, tmp) != team:
                return False
        return True

    def check_north_west(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        tmp2: int = insY
        for ind in range(3):
            tmp -= 1
            tmp2 -= 1
            if tmp == 0 or tmp2 == 0:
                return False
            if self.board.get_square(tmp2, tmp) != team:
                return False
        return True

    #check_south_west backchecks its diagonal
    def check_south_west(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        tmp2: int = insY
        count: int = 0
        atEnd: bool = False
        for ind in range(3):
            tmp -= 1
            tmp2 += 1
            if tmp == 0 or tmp2 == self.board.get_length():
                atEnd = True
                break
            if self.board.get_square(tmp2, tmp) != team:
                atEnd = True
                break
            else:
                count += 1
        if atEnd:
            tmp = insX
            tmp2 = insY
            for ind in range(3-count):
                tmp += 1
                tmp2 -= 1
                if tmp == self.board.get_width() or tmp2 == 0:
                    return False
                if self.board.get_square(tmp2, tmp) != team:
                    return False
        return True


    # check_south_east backchecks it's diagonal
    def check_south_east(self, insY: int, insX: int, team: str) -> bool:
        tmp: int = insX
        tmp2: int = insY
        count: int = 0
        atEnd: bool = False
        for ind in range(3):
            tmp += 1
            tmp2 += 1
            if tmp == self.board.get_width() or tmp2 == self.board.get_length():
                atEnd = True
                break
            if self.board.get_square(tmp2, tmp) != team:
                atEnd = True
                break
            else:
                count += 1
        if atEnd:
            tmp = insX
            tmp2 = insY
            for ind in range(3-count):
                tmp -= 1
                tmp2 -= 1
                if tmp == 0 or tmp2 == 0:
                    return False
                if self.board.get_square(tmp2, tmp) != team:
                    return False
        return True
            
        



