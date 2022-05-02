import numpy as np
import math 
with open('../data/smoke_basin') as f:
    lines = f.readlines()
    
data = np.array([[int(i) for i in line.strip()] for line in lines])

num_rows, num_cols = len(data), len(data[0])

basin_counts = []

def increase_basin(row,col):
    # basin spread stops for these conditions: 1) square boundary reached, 2) square counted already, 3) square is value 9
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols or data[row][col]== -1 or data[row][col]==9:
        return
    data[row][col] = -1 # mark square as counted
    basin_counts[-1] += 1 #
    # Iterate for surrounding squares recursively
    new_locs = [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]
    for new_loc in new_locs:
        increase_basin(new_loc[0],new_loc[1])
            

for row in range(num_rows):
    for col in range(num_cols):
        basin_counts += [0]
        increase_basin(row,col)
        
basin_counts_sorted = sorted([i for i in basin_counts if i!=0])
print(math.prod(basin_counts_sorted[-3:]))
        
    

        
        
    