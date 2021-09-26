import pygame
class S_Piece:
    def __init__(self):
        self.rotation = 0
        self.in_motion = True
        self.row = 0 #this would be the initial row that it starts and is in terms of the grid template rather than the piece template
        #this is the pivot block, so it remains in place when only rotating, aka the shape rotates about this block
        #set it as row 1 because some of the shapes like Z and T have a block on top of it so initial row cannot be 0
        self.column = 4 # initial column is 4 because it is in the middle of the grid (columns are from 0-9 not 1-10)
        self.config = [[(2,0),(0,1),(1,0),(1,1)],[(0,0),(1,2),(0,1),(1,1)]]
        self.color = (110,234,32)
        self.piece = self.config[0]
        self.prev_row = None
        self.prev_column = None
        self.rotated=False
    def update(self):
        #should be moving down everytime
        self.prev_location()
        self.row += 1
    def move_left(self):
        self.prev_location()
        self.column -= 1
    def move_right(self):
        self.prev_location()
        self.column += 1
    def rotate(self):
        self.prev_location()
        self.rotation += 1
        self.rotation%=len(self.config)
        self.piece=self.config[self.rotation]
        self.rotated = True

    def counter_rotate(self):
        #self.piece = self.config[(self.config.index(self.rotation)-self.index)%len(self.piece)]
        self.rotation -= 1
        self.rotation%=len(self.config)
        self.piece=self.config[self.rotation]
        self.rotated=False
    def prev_location(self):
        self.prev_row = self.row
        self.prev_column = self.column
    def prev_config(self):
        index = self.rotation - 1
        index%=len(self.config)
        return [(y+self.row,x+self.column) for x,y in self.config[index]]
    def next_config(self):
        index = self.rotation + 1
        index%=len(self.config)
        return [(y+self.row,x+self.column) for x,y in self.config[index]]
