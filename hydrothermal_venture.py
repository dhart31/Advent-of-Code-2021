import numpy as np
import re

class Coordinates:
    def __init__(self):
        self.coordinates = None
    
    def load_coordinates(self,filename):
        f = open(filename)
        lines = f.readlines()
        f.close()
        self.coordinates = np.zeros((len(lines),4),dtype=int)
        for row_idx,line in enumerate(lines):
            line = line.strip()
            self.coordinates[row_idx,:] = ([int(i) for i in re.split('-> |,',line)]) # Split lines by -> or , with regular exp

    def get_vals(self,a,b):
        if b > a:
            return np.arange(a,b+1)
        else:
            return np.arange(a,b-1,-1)
    
    def count_overlap_points(self,count_diagonals=False):
        # Make grid spanning the coordinate range
        max_val = np.amax(self.coordinates)+1
        grid = np.zeros((max_val,max_val))      
        for coord in self.coordinates:
            x1,y1,x2,y2  = coord[0],coord[1],coord[2],coord[3]             
            if x1 == x2:
                grid[self.get_vals(y1,y2),x1] +=1
            elif y1 == y2:
                grid[y1,self.get_vals(x1,x2)] +=1
            # For part 2
            elif count_diagonals:
                grid[self.get_vals(y1,y2),self.get_vals(x1,x2)] += 1
        return np.sum(grid>1)      
            
 
coords = Coordinates()
coords.load_coordinates('../data/coordinates')

# PART 1
print(coords.count_overlap_points())
# PART 2
count_diagonals=True
print(coords.count_overlap_points(count_diagonals))

    