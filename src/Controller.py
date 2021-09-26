import random
import sys
import pygame as pg
from src.grid import grid
from src.I_Piece import I_Piece
from src.J_Piece import J_Piece
from src.T_Piece import T_Piece
from src.Z_Piece import Z_Piece
from src.L_Piece import L_Piece
from src.S_Piece import S_Piece
from src.O_Piece import O_Piece

class Controller():
    #initializes the game
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800,900))
        self.background = pg.Surface(self.screen.get_size()).convert()
        self.rect = self.background.get_rect()
        pg.display.set_caption("Tetris")
        self.clock = pg.time.Clock()
        self.mytext = pg.font.SysFont('Comic Sans MS', 30)
        self.state = "GAME"
        self.list_of_shapes = [S_Piece, T_Piece, Z_Piece, I_Piece, L_Piece, O_Piece, J_Piece]
        self.falling_piece = None
        self.main_grid = grid()
    #Game loop is respond to event, update models, redraw screen
    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()


    def gameOver(self):

        pg.quit()
        sys.exit()

    def gameLoop(self):
        self.text2 = self.mytext.render("press something on your keyboard to begin playing !!!!", True, (255, 255, 255))
        self.screen.blit(self.text2,(0,0))
        pg.display.flip()
        for gogo in pg.event.get():
            if(gogo.type == pg.KEYDOWN):
                #display "press any key to start the game"
                while(self.state == "GAME"):
                    if(self.falling_piece == None):
                        self.falling_piece = self.get_new_piece()
                        self.initialize_to_grid(self.falling_piece)
                        #self.events()
                    else:
                        if(self.droppable(self.falling_piece)):
                            self.falling_piece.update()
                            self.main_grid.update(self.falling_piece)
                        else:
                            self.add_to_grid(self.falling_piece)
                            self.main_grid.clear_row()
                        self.events()
                    self.screen.blit(self.background,(0,0))
                    self.draw_lines() #draws visual board with lines
                    self.draw_grid()
                    self.textsurface = self.mytext.render('Lines Sent:' + str(int(self.main_grid.score/10)), True, (255, 255, 255))
                    self.screen.blit(self.textsurface,(0,0))
                    pg.display.flip()
                    self.clock.tick(7)
    #Game Loop -  events
    def events(self):
           #check for closing window
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                sys.exit()
            elif(event.type == pg.KEYDOWN):
                if(self.falling_piece != None):
                    if(event.key == pg.K_UP):
                        move_rotate = self.falling_piece.next_config()
                        if(self.droppable(self.falling_piece)):
                            if(self.is_valid(move_rotate,self.falling_piece)):
                                self.falling_piece.rotate()
                                self.main_grid.update(self.falling_piece)
                        else:
                            self.add_to_grid(self.falling_piece)
                            self.main_grid.clear_row()
                            self.main_grid.update(self.falling_piece)
                    elif(event.key == pg.K_LEFT):
                        move_left = [(self.falling_piece.row+y,self.falling_piece.column+x-1) for x,y in self.falling_piece.piece]
                        if(self.droppable(self.falling_piece)):
                                if(self.is_valid(move_left,self.falling_piece)):
                                    self.falling_piece.move_left()
                        else:
                            self.add_to_grid(self.falling_piece)
                            self.main_grid.clear_row()
                        self.main_grid.update(self.falling_piece)
                    elif(event.key == pg.K_RIGHT):
                        move_right = [(self.falling_piece.row+y,self.falling_piece.column+x+1) for x,y in self.falling_piece.piece]
                        if(self.droppable(self.falling_piece)):
                            if(self.is_valid(move_right,self.falling_piece)):
                                self.falling_piece.move_right()
                        else:
                            self.add_to_grid(self.falling_piece)
                            self.main_grid.clear_row()
                        self.main_grid.update(self.falling_piece)
                    elif(event.key == pg.K_SPACE):
                        while(self.droppable(self.falling_piece)):
                            self.falling_piece.update()
                            self.main_grid.update(self.falling_piece)

    def draw_lines(self):
        for x in range(11):
            x = x*32+160
            pg.draw.line(self.screen, (255, 255, 255), (x, 160), (x, 800))
        for y in range(21):
            y = y*32+160
            pg.draw.line(self.screen, (255, 255, 255), (160, y), (480, y))

    def is_valid(self, movement, piece): # movement is a list of 4 coordinates of the requested position of the grid, and piece is just the piece that is requesting the move
        count = 0
        for xcor, ycor in movement:
            if(xcor>19):
                return False
            if (ycor<0 or ycor>9):
                return False
            if (self.main_grid.grid[xcor][ycor] == None):
                count +=1
            elif (self.main_grid.grid[xcor][ycor] == piece.color): #this case is for when one or more of the pieces' block itself is in the space that
            #its intending to move into, aka when the O block is trying to go anywhere, or when the L piece is going down, etc
                count += 1
        if (count == 4): #if all 4 blocks are empty, then count would be 4. this means the space the piece wants to move to is empty.
            return True
        else:
            return False

    def get_new_piece(self):
        return random.choice(self.list_of_shapes)()
    def add_to_grid(self, piece):
        #adds to the piece to the board so that the piece's coordinates stay, and right after get_new_piece() should be called
        #args is the piece that is to be added to the grid
        for x,y in piece.piece:
            self.main_grid.grid[piece.row+y][piece.column+x] = (0, 255, 255) #make the added to board ones a different color
        move_left = [(self.falling_piece.row+y,self.falling_piece.column+x-1) for x,y in self.falling_piece.piece]
        move_right = [(self.falling_piece.row+y,self.falling_piece.column+x+1) for x,y in self.falling_piece.piece]
        move_rotate = [(self.falling_piece.row+y,self.falling_piece.column+x) for x,y in self.falling_piece.piece]
        self.falling_piece = None
    def initialize_to_grid(self, piece):
        #initializes the piece to the board and updates the board's elements with the corresponding elements in the piece
        #this method is different from add_to_grid
        #add_to_grid is when the piece lands, initialize_to_grid is when the piece is generated and starts
        #parameter is same as add_to_grid parameters
        initialization = [(self.falling_piece.row+y,self.falling_piece.column+x) for x,y in piece.piece]
        if(self.is_valid(initialization,piece)):
            #check if piece can be put onto board or not
            for x,y in initialization:
                self.main_grid.grid[x][y] = piece.color
                #i defined the configs of the shape
                # to be x,y instead of row,column, which is how the grid is defined, thats why i do row+y and column+x instead of row+x, column+y
        else:
            self.state = "GAMEOVER"
    def droppable(self,piece):
        if piece == None:
            return False
        move_list  = [(self.falling_piece.row+y+1,self.falling_piece.column+x) for x,y in piece.piece]
        return self.is_valid(move_list, piece)
        ##this checks if the movement is downwards, and if it returns False that means there is something beneath it so add it to the board
    def draw_grid(self):
        tile = pg.Surface((28,28))
        for i in range(20):
            for j in range(10):
                if (self.main_grid.grid[i][j] != None): #there is a RGB color
                    tile.fill(self.main_grid.index(i,j))
                elif (self.main_grid.grid[i][j] == None): # there is no RGB color
                    tile.fill((0,0,0))
                self.screen.blit(tile,(160+j*32+2,160+i*32+2))
