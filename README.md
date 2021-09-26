# Tetris

## Project Description
Classical Tetris Game, with traditional arrow keys as movement commands as well as space bar as the hard drop. Row clears when it is full, and game ends when it stacks to the top.

## User Interface Design

* A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program.
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
    * You should also have a screenshot of your final GUI

***        

## Program Design

* Decide upon a class interface for the classes in your project.
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example).
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* You should have a list of each of your classes with a description.

***

## Testing

### Menu Testing
When the game is run from command prompt, it should display a text that prompts the user to press a key to start the game.
Test all/any key to start the game.

### Game Testing
After the user presses any key and the game starts, a random shape should be generated and falling down from top to bottom. Use traditional arrow keys on keyboard to test the movement of the falling piece. The piece should not go off the screen.

Pressing up key rotates the piece, and pressing spacebar would 'hard drop' the piece, moving it to the nearest bottom. Once it hits the nearest bottom surface, it should become a different color that is distinct from the falling piece. Also once it is added to the bottom, player should no longer be able to control it, and a new controllable piece should be generated at the top of the screen.

Every time a row is filled, it should clear up, the entire grid and everything contained inside should shift down, and on the top, the score aka the lines sent, should also be increasing proportional to the number of rows cleared.

Once there is no more room for the new piece to be generated, the game should end.

| Step                       | Procedure     | Expected Results  | Actual Results |
| ----------------------     |:-------------:| -----------------:| -------------- |
|  1  | Run Controller       | Press any button display text      | -----------------|
|  3  | Press any key        | Game starts    |                  |
|  4  | left arrow           | piece moves left|                 |
|  5  | right arrow          | piece moves right |               |
|  6  | up arrow             | piece rotates |                   |
|  7  | down arrow           | piece moves down|                 |
|  8  | space bar            | piece drops down|                 |
|  9  | general playtesting  | normal tetris|                     |
|  10  | win state           | none, until user loses |                |


