import numpy as np
import re

with open('../data/transparent_origami') as f:
    lines = f.read().splitlines()
    
lines.remove("")
dot_locations = []
fold_locations = []
# Parse folding instructions as well as initial dot coordinates
for line in lines:
    if 'fold' in line:
        val = [int(i) for i in re.findall(r'\d+',line)]
        if 'x' in line:            
            fold_locations += [[val[0],0]]
        else:
            fold_locations += [[0,val[0]]]
    else:
        dot_locations+=[[int(i) for i in line.split(',')]]
        
dot_locations = np.array(dot_locations)
fold_locations = np.array(fold_locations)

width = fold_locations[0][0]*2+1 # Get the initial width, where the first fold is the middle value of the square
dot_array = np.zeros((width,width))


for loc in dot_locations:
    dot_array[loc[1],loc[0]]=1

for fold_loc in fold_locations:
    x,y = fold_loc[0],fold_loc[1]
    if x!=0:
        left = dot_array[:,:x] #  Stop before middle crease
        right = np.flip(dot_array[:,x+1:2*x+1],1) # continue after middle crease
        dot_array = np.logical_or(left,right)
               
    else:
        up = dot_array[:y,:] # do the same for y axis
        down = np.flip(dot_array[y+1:2*y+1,:],0)   
        dot_array = np.logical_or(up,down)

for line in dot_array:
    line_print =''
    for char in line:
        if char:
            line_print += '#'
        else:
            line_print += '.'
    print(line_print+' ')
        