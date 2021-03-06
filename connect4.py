from board import *
from utility import *
import pdb

class Play:
    def __init__(self):
        self.board = self.new_game() 
        self.utilities = Utility(self.board)

    def play(self):
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
        win: bool = False
        notValid: bool = True
        print(f"\n{team}'s turn")
        while notValid:
            column = input("pick a column to place a tile in: ")
            if ord(column.upper()) >= ord('A') and ord(column.upper()) - ord('A') <= self.board.get_width() -1:
                notValid = False
        indX = int(ord(column.upper()) - ord('A'))
        [insX, insY] = self.board.insert_piece(team, indX)
        self.board.print_board()
        if [insX, insY] == [-1, -1]:
           return win
        win = self.utilities.check_win(insX, insY, team)
        if win:
            print(f"\nCongratulations {team} you won")
        return win

    def new_game(self) -> None:
        length = input("how long would you like your game board to be: ")
        width = input("how wide would you like your game board to be: ")
        return Board(int(length), int(width))

    def play_again(self) -> bool:
        playAgain: str = input("would you like to play again y/n: ")
        if playAgain == "y":
            self.new_game()
            return True
        else:
            quit()

    
    



p = Play()
p.play()
