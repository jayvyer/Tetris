import pygame
class J_Piece:
    def __init__(self):
        self.rotation = 0
        self.in_motion = True
        self.row = 0
        self.column = 4
        self.config = [[(0,2),(1,0),(1,2),(1,1)],[(0,0),(0,1),(2,1),(1,1)],[(1,0),(2,0),(1,2),(1,1)],[(0,1),(2,2),(2,1),(1,1)]]
        self.color =  (197,66,244)
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
