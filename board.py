import pdb
from utility import *
import sys

class Board:
    def __init__(self, length: int, width: int) -> None:
        self.length: int = length
        self.width: int = width
        self.board: List[List] = [['-' for i in range(self.width)] for j in range(self.length)]
        self.utilities: Utility = Utility(self.board)

    def insert_piece(self, team: str, xInd) -> List[int]:
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
        return self.board

    def get_length(self) -> int:
        return self.length #note that this is +1 on the index  

    def get_width(self) -> int:
        return self.width

    def get_square(self, yInd, xInd) -> chr:
        return self.board[yInd][xInd]

    def set_square(self, yInd, xInd, value: str) -> None:
        self.board[yInd][xInd] = value

    def print_board(self) -> None:
        for ind, spots in enumerate(self.get_board()):
            for spot in spots:
                print(spot, end = " ")
            print("\n")
        for xInd in range(self.width):
            print(chr(xInd + ord('A')), end = " ")
                    


