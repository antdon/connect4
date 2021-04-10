from board import *
from typing import List, Set, Dict, Tuple, Optional

class Utility:
    """
    Made up of utility functions used acting on the board passed into the class
    when Utility is initialised
    It is important that when board is reinitialized Utility is reinitialised
    with the new board
    Parameters:
        board - List[List] that represents the board in the current game state
    """
    def __init__(self, board: List[List]) -> None:
        self.board: Board = board

    def check_full(self, xInd: int) -> None:
        """
        Check to see every square in the column corresponding to xInd has been
        filled
        Parameters:
            xInd - column that is being checked
        """
        if self.board[0][xInd] == '-':
            return False
        else:
            return True

    def check_if_edge(self, insY: int, insX: int) -> List[str]:
        """
        Check to see if specified square is on an edge
        Parameters:
            insY - y index of the piece being checked
            insX - x index of the piece being checked
        Return:
            a list containing compass directions of the edges the checked piece
            sits on
            list should not contain more than 2 elements
        """
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
        """
        Takes the most recently inserted piece and checks to see if this piece 
        caused the player who placed the piece to connect 4
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
        Return:
            True if a win has been achieved 
            False if win has not been achieved
        """
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


    def check_potential_win_directions(
            self,
            insY: int, 
            insX: int, 
            dontCheck: List[str],
            team: str) -> List[str]:
        """
        Returns a list of compass directions showing the directions 
        in which a square of the same type to the placed piece lies 
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            dontCheck - List of directions to avoid due to edges
            team - string representing the team that placed the piece
        Return:
            List of directions in which a sqare of the same type to the
            placed piece lie
        """
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
        """
        Checks north for 4 in a row from and including the inserted piece
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
        tmp: int = insY
        for ind in range(3):
            tmp -= 1
            if tmp == 0:
                return False
            if self.board.get_square(tmp, insX) != team:
                return False
        return True

    def check_south(self, insY: int, insX: int, team: str) -> bool:
        """
        Checks south for 4 in a row from and including the inserted piece
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
        tmp: int = insY
        for ind in range(3):
            tmp += 1
            if tmp == self.board.get_length():
                return False
            if self.board.get_square(tmp, insX) != team:
                return False
        return True

    def check_east(self, insY: int, insX: int, team: str) -> bool:
        """
        Checks east for 4 in a row from and including the inserted piece
        Backchecks for mid 4 insertions 
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
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
        """
        Checks west for 4 in a row from and including the inserted piece
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
        tmp: int = insX
        for ind in range(3):
            tmp -= 1
            if tmp == 0:
                return False
            if self.board.get_square(insY, tmp) != team:
                return False
        return True

    def check_north_east(self, insY: int, insX: int, team: str) -> bool:
        """
        Checks north east for 4 in a row from and including the inserted piece
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
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
        """
        Checks north-west for 4 in a row from and including the inserted piece
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
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

    def check_south_west(self, insY: int, insX: int, team: str) -> bool:
        """
        Checks south west for 4 in a row from and including the inserted piece
        Backchecks for mid 4 insertions 
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
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


    def check_south_east(self, insY: int, insX: int, team: str) -> bool:
        """
        Checks south east for 4 in a row from and including the inserted piece
        Backchecks for mid 4 insertions 
        Parameters:
            insY - y index of the inserted piece
            insX - x index of the inserted piece
            team - string representing the team that placed the piece
        Return:
            True if finds 4 in a row
            False otherwise
        """
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
            
        



