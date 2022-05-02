import re
import numpy as np
import itertools


lines = open("../data/reactor_robot").read().splitlines()

switches = []
steps = []
for line in lines:
    linedata = line.split(' ')
    if linedata[0] == 'off':
        switch_val = 0
    else:
        switch_val = 1
    cube_ranges = [int(i) for i in re.findall(r'-?\d+',linedata[1])] # Get reactor coordinate ranges, s
    np.insert(cube_ranges,0,switch_val)
    steps += [[switch_val]+cube_ranges]
    
# # Part 1 naive method
# cubes = {}
# for step in steps:
    # s = step
    # coordinates = [list(range(s[1],s[2]+1)),list(range(s[3],s[4]+1)),list(range(s[5],s[6]+1))]
    # if s[0] == 1:
        # for c in list(itertools.product(*coordinates)):
            # cubes[c] = 1
    # else:
        # for c in list(itertools.product(*coordinates)):
            # cubes[c] = 0
                    
# print(sum(cubes.values()))

def intersection(s,t):
    # Each range vector, s & t, specifies lower and upper bounds of x,y,z
    # Intersections include the max of lower bounds, and min of upper bounds
    # In final sum, the first element will specify whether to subtract or add the coordinates
    #                      xvals                         yvals                         zvals
    
    x_lb, x_ub = max(s[1],t[1]),min(s[2],t[2])
    y_lb, y_ub = max(s[3],t[3]),min(s[4],t[4]) 
    z_lb, z_ub = max(s[5],t[5]),min(s[6],t[6]) 
    n = [-t[0],x_lb,x_ub,y_lb,y_ub,z_lb,z_ub]
    
    # if the min is larger than the max for any coordinate, there is no intersection, return none
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n
    
cubes = []
for step in steps:
    # If step gives 'on' instruction, add cuboid to chunk
    if step[0] == 1:
        chunks = [step]
    # If step gives 'off' instruction, don't add it
    else:
        chunks = []
    
    # For each step, check if the new chunk overlaps with stored cubes
    for cube in cubes:
        overlap = intersection(step,cube)
        #If there is an overlap, add a new cube to the chunks specifying the overlap
        #If the step gives 'off' instruction, the cube will be 'negative' and subtract the volume from the cubes
        if overlap:
            chunks += [overlap]
            
    # Add the new chunks to all the already existing cubes in the volume
    cubes += chunks
    
count = 0
for c in cubes:
    count += c[0]*(c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
    
print(count)

    
