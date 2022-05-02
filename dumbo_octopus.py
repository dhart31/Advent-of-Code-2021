import numpy as np

with open('../data/dumbo_octopus_test') as f:
    lines = f.read().splitlines()
    data = np.zeros((len(lines),len(list(lines[0]))))
    for row_idx,line in enumerate(lines):
        data[row_idx,:] = (np.array([int(i) for i in list(line)]))
    
num_rows, num_cols = len(data), len(data[0])

def get_flash_idxs(idxs):
    flash_idxs = []
    for i in range(len(idxs)):
        for j in range(len(idxs[0])):
            if idxs[i,j]:
                flash_idxs += [[i,j]]
    return(flash_idxs)

def out_of_bounds(row,col):
    return row < 0 or row >= num_rows or col < 0 or col >= num_cols

num_flashes = 0
def flash(data,row,col):
    data[row,col] = 0
    # Get locations of all 8 neighbors surrounding square
    new_locs = [[row-1,col-1],[row-1,col],[row-1,col+1],[row,col-1],[row,col+1],[row+1,col-1],[row+1,col],[row+1,col+1]] 
    # Dont increase locations that have already flashed or are out of bounds
    for new_loc in new_locs:
        if not out_of_bounds(new_loc[0],new_loc[1]) and data[new_loc[0],new_loc[1]]!=0:
            data[new_loc[0],new_loc[1]] += 1
    return data
    
steps = 0
while not np.all(data==0):
    steps+=1
    data +=1
    flash_idxs = get_flash_idxs(data>9)
    while flash_idxs:
        for flash_idx in flash_idxs:
            num_flashes += 1
            data = flash(data,flash_idx[0],flash_idx[1])
        flash_idxs = get_flash_idxs(data>9) # Allow for flash chain reaction

print(steps)
                