import pdb
from utility import *
import sys

class Board:
    def __init__(self, length: int, width: int) -> None:
        """
        Initialise a new board object. 
        Indexed such that (0,0) is in the top left hand corner.
        """
        self.length: int = length
        self.width: int = width
        self.board: List[List] = [['-' for i in range(self.width)] for j in range(self.length)]
        self.utilities: Utility = Utility(self.board)

    def insert_piece(self, team: str, xInd) -> List[int]:
        """
        Sets the square with the smallest y index to the str team, noting that
        the board is indexed such that (0,0) is in the top left hand corner.
        Parameters:
            team - the team that is playing the piece 'X' or 'O'
            xInd - the x index of the column in which the piece would be played
        Return:
            a list containing the y and x index of the square in which 
            the piece landed
        """
        if(self.utilities.check_full(xInd)):
            print("this column is full", file=sys.stderr)
            return [-1, -1]
        insertionY: int = -1
        insertionX: int = -1
        for yInd in range(self.length):
            if self.get_square(yInd, xInd) == '-':
                insertionY = yInd
                insertionX = xInd
        if insertionY == -1 and insertionX == -1:
           return [-1, -1]
        self.set_square(insertionY, insertionX, team)
        return [insertionY, insertionX]

    def get_board(self) -> List[List]:
        """Return:
            the 2D array representing the board in the current game state"""
        return self.board

    def get_length(self) -> int:
        """Return:
            the length of the 2D array representing the board in the 
            current game state"""
        return self.length #note that this is +1 on the index  

    def get_width(self) -> int:
        """Return:
            the width of the 2D array representing the board in the current 
            game state"""
        return self.width

    def get_square(self, yInd, xInd) -> chr:
        """
        Parameters:
            yInd - y index of the required square
            xInd - x index of the required square
        Return:
            the char value that is at the x and y parameters in 
            current state of the board
        """
        return self.board[yInd][xInd]

    def set_square(self, yInd, xInd, value: str) -> None:
        """
        Sets a specific square to a specific value
        Parameters:
            yInd - y index of the required square
            xInd - x index of the required square
            value - value to set the square to
        Return:
            None
        """
        self.board[yInd][xInd] = value

    def print_board(self) -> None:
        """
        prints the current board state to stdout
        Return:
            None
        """
        for ind, spots in enumerate(self.get_board()):
            for spot in spots:
                print(spot, end = " ")
            print("\n")
        for xInd in range(self.width):
            print(chr(xInd + ord('A')), end = " ")
                    


