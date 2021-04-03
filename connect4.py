from board import *
from utility import *
import pdb

class Play:
    """
    Contains exclusively functions called by run.py
    """
    def __init__(self) -> None:
        """initialise a new board and a new utility class taking the board as a parameter"""
        self.board: Board = self.new_game() 
        self.utilities: Utility = Utility(self.board)

    def play(self) -> None:
        """Play an instance of the game"""
        stillPlaying: bool = True
        notOver: bool = True
        while stillPlaying:
            self.board.print_board()
            while notOver:
                if(self.turn('X')):
                    break
                if(self.turn('O')):
                    break
            stillPlaying = self.play_again()



    def turn(self, team: str) -> bool:
        """
        Represents one players turn
        Parameters:
            team - string representing the team of the player
        Return:
            Returns whether the player won the game in this turn
        """
        win: bool = False
        notValid: bool = True
        insX: int
        insY: int
        print(f"\n{team}'s turn")
        while notValid:
            column = input("pick a column to place a tile in: ")
            if len(column) == 0 or len(column) > 1:
                continue
            if ord(column.upper()) >= ord('A') and ord(column.upper()) - ord('A') <= self.board.get_width() -1:
                notValid = False
        indX: int = int(ord(column.upper()) - ord('A'))
        [insX, insY] = self.board.insert_piece(team, indX)
        self.board.print_board()
        if [insX, insY] == [-1, -1]:
           return win
        win = self.utilities.check_win(insX, insY, team)
        if win:
            print(f"\nCongratulations {team} you won")
        return win

    def new_game(self) -> Board:
        """
        Creates a new game with a board of a inputted size
        Return:
            The board of the new game
        """
        notValid: bool = True
        notValid2: bool = True
        while notValid:
            length: str = input("how long would you like your game board to be (> 4): ")
            if length.isdigit() and int(length) > 4:
                notValid = False
        while notValid2:
            width: str = input("how wide would you like your game board to be (> 4): ")
            if width.isdigit() and int(width) > 4:
                notValid2 = False
        return Board(int(length), int(width))

    def play_again(self) -> bool:
        """
        Gives player option to player again and if yes reinitialises the game board and utility function
        Return:
            True if player chooses to play again
            False otherwise
        """
        notValid: bool = True
        while notValid:
            playAgain: str = input("would you like to play again y/n: ")
            playAgain = playAgain.lower()
            if playAgain == "y" or playAgain == "n":
                notValid = False
        if playAgain == "y":
            self.board = self.new_game()
            self.utilities = Utility(self.board)
            return True
        else:
            quit()
            return False

    
    

