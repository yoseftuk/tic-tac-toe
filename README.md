# Tic-Tac-Toe
tic-tac-toe vs computer pythn game

### Run the project
 * Download project files
 * From the project directory run `python index.py`
 
### Rules
 * Tap on any of the free squares to make your turn
 * Tap anywhere on the screen to start a new game
 
 ### Project structure
  * ***gui.py*** - working with the gui - open the window, draw the board, draw the *X*, and *O* and handle the user clicks
  * ***game_tree.py*** - build the game tree (data for all the possible turns with its stats)
  * ***index.py*** - manage the progress of the game using te above tools
  
### The Algorithm
 #### *Buiding the game tree*
 From the starting position, where all the squares are free (value *0*), we iterate for all the free squares (value 0), and for each one add a child option where the next turn fill this square (-1 for *X*, 1 for *O*).
 
 Each option is a subtree of all the possible options from this point, so the same function are called, with the base position as the next option, instead of the starting position.
 
 The exit point from this recursion is: 
 
  **1.** if one of the sides win,
  
  **2.** if no free squares left.
 #### *Ceching the options*
 Because the same position have the same subtree of options regardless of how the players come to this position, it's westful to caculate it's again.for this propose during the game-tree building each position first checked in a ceche object, and if it's exist there the value pulled fromtheerre, instead of calculating again. If not it'scalculate it, and add the subtree to the ceche, for reduce the future calculation
 #### *Calculating computer strategy*
 For the very last turn it's easy to make a desicion - if we mark as 1 the turn where the computer win, 0 on draw and -1 when the user win, the smartest turn for the computer is the turn with the maximum value.
 
 For one turn before (computer go, then the user make the final turn) we can give a value for each of the pre-last turn as the minimum value from it's next turn values (which will be the smartest turn for the user), then the turn for the maximun value will be the smarter for the computer.
 
 This way we can go up till the very start of the game - each option get the value of the maximun values of it's children, which value is the minimum value of it's children, which value is the maximum of it's children, etc. till the tails, where the value is 1 for computer win, 0 for draw and -1 for user win (the turn of the computer calculated as the maximum from the next options, because the computer make the choise, and he interested to get the maximum score, but calculated as a minimum value where it's turn of the user, because the user make the choise, and he interesting to get the minimum of possible values)
