import pygame
class T_Piece:
    def __init__(self):
        self.rotation = 0
        self.in_motion = True
        self.row = 0
        self.column = 4
        self.config = [[(1,0),(0,1),(2,1),(1,1)],[(1,0),(1,2),(2,1),(1,1)],[(0,1),(2,1),(1,2),(1,1)],[(1,0),(0,1),(1,2),(1,1)]]
        self.color = (234,32,32)
        self.piece = self.config[0]
        self.prev_row = None
        self.prev_column = None
        self.rotated=False
    def update(self):
        '''
            moves the piece one row down
            args: none
            return: none
        '''
        #should be moving down everytime
        self.prev_location()
        self.row += 1
    def move_left(self):
        '''
            moves the piece one column left
            args: none
            return: none
        '''
        self.prev_location()
        self.column -= 1
    def move_right(self):
        '''
            moves the piece one column right
            args: none
            return: none
        '''
        self.prev_location()
        self.column += 1
    def rotate(self):
        '''
            rotates the piece to the next configuration
            args: none
            return: none
        '''
        self.prev_location()
        self.rotation += 1
        self.rotation%=len(self.config)
        self.piece=self.config[self.rotation]
        self.rotated = True

    def counter_rotate(self):
        '''
            rotates the piece to the previous configuration, only used to counter rotate when a rotated piece's position is invalid
            args: none
            return: none
        '''
        self.rotation -= 1
        self.rotation%=len(self.config)
        self.piece=self.config[self.rotation]
        self.rotated=False
    def prev_location(self):
        '''
            keeps track of the previous location of the block
            args: none
            return: none
        '''
        self.prev_row = self.row
        self.prev_column = self.column
    def prev_config(self):
        '''
            keeps track of the previous configuration of the block
            args: none
            return: none
        '''
        index = self.rotation - 1
        index%=len(self.config)
        return [(y+self.row,x+self.column) for x,y in self.config[index]]
    def next_config(self):
        '''
            keeps track of the next location of the block
            args: none
            return: none
        '''
        index = self.rotation + 1
        index%=len(self.config)
        return [(y+self.row,x+self.column) for x,y in self.config[index]]
