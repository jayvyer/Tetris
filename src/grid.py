class grid:
    def __init__(self):
        self.grid =  [[None for column in range(10)] for row in range(20)] #creates a grid that is indexed through grid[row][column] to find something
        self.score = 0
    def index(self,i,j):
        '''
            find index of the grid, basically the __str__
            args: row, column or integers
            return: element in that grid[row][column]
        '''
        return self.grid[i][j]
    def clear_row(self):
        self.count = 0
        self.full_rows = {}
        row_shift = []
        for i in range(20):
            self.full = 0  #everytime it goes to a new row, the count will start at 0
            for j in range(10):
                if (self.grid[i][j] != None):
                    self.full += 1
                    self.full_rows[i] = self.full #dictionary will contain the row, and how many pieces are filled up in that row
        for row in self.full_rows:
            if(self.full_rows[row] == 10): #this means that the row is full
                for column in range (10):
                     self.grid[row][column] = None #set everything in that row to be empty
                     self.count += 1
                row_shift+=[row]
        self.grid_shift_down(sorted(row_shift,reverse=True)) #if multiple lines are cleared at once, this keeps track of how many times to shift the grid down
        self.score += self.count
    def grid_shift_down(self,row_shift):
        '''
            shifts down the grid once a row is full
            args: row shift is the rows that needed to be shifted down
            return: none
        '''
        #should be called after each clear_row, since everything on the grid has to be shifted down vertically
        #this means that everything in the row becomes the corresponding value on directly above it aka the same column but different row
        count = 0
        for i in row_shift:
            i -= count
            for row in range(i,0,-1):
                for column in range(10):
                    self.grid[row][column] = self.grid[row-1][column]
            count+=1


    def update(self,piece): #current position will be 4 coordinates
        '''
            updates the grid so that the intended position of the piece is on the grid, and the previous location of the piece is released
            args: piece that is falling
            return: none
        '''
        if piece == None:
            return
        #should be called after every event so that the previous position of the piece will be set to NONE and the piece moves to the intended location
        self.release_location(piece)
        for x,y in piece.piece:
            if(piece.row+y>19):
                piece.row -=y
            if(piece.column+x>9):
                piece.column -= x
            self.grid[piece.row+y][piece.column+x] = piece.color

    def release_location(self,piece):
        '''
            releases the location of the previous piece
            args: falling piece
            return: none
        '''
        if (piece.rotated == False):
            r = piece.prev_row
            c = piece.prev_column
            for x,y in piece.piece:
                self.grid[r+y][c+x] = None
        else:
            temp = piece.prev_config()
            if temp != None:
                for x,y in temp:
                    self.grid[x][y] = None
            piece.rotated = False
