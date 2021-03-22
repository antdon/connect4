## How To Run
cd into the cloned dir

run
```
python3 connect4
```

## Project Summary
Connect4 is based on the classic board game of the same title. This project is a simple version of the game that can be played between two players in the terminal of a singular machine. Future iterations of this project will likely include a bot that can play the game against a user with the possiblity of increasing the difficulty of the bot untill it reaches the [perfect connect four startegy](http://web.mit.edu/sp.268/www/2010/connectFourSlides.pdf) as the highest difficulty.

## Implementation
The game is implemented using a 2d array. When a new piece is inseted into the board at a specific column it will fill the lowest available row in the column with the character representing the team that placed the piece. When a piece is played the squares surrounding the square in which it lands are checked for characters of the same team as the piece inserted. The directions in which these same team pieces appear are added to a list of potential win directions. Each of these are then checked for four in a row. Each diagonal and the vertical direction have an additional check for mid four insertion wins. These additional checks do not need to to be implemented in every direction check because if a mid four insertion win occurs it is a necessary condition that both directions of diagonal or horizontal axis are filled.

## Example Game
<table><tr>
<td> <img src="https://github.com/antdon/connect4/blob/main/connect4_example.png" alt="Drawing" style="width: 250px;"/> </td>
<td> <img src="https://github.com/antdon/connect4/blob/main/connect_4_example2.png" alt="Drawing" style="width: 250px;"/> </td>
</tr></table>

