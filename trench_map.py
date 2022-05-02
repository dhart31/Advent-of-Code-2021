import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from scipy.ndimage import convolve
with open("../data/trench_map_test") as f:
    algorithm_str = f.readline().strip()
    f.readline()
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]

#Convert algorithm string into 512 bit binary array
algorithm = np.zeros(len(algorithm_str),dtype=int)
for i,char in enumerate(algorithm_str):
    if char == '.':
        algorithm[i] = 0
    else:
        algorithm[i] = 1
#Convert image string into 2d array 
data = np.zeros((len(lines),len(lines[0])),dtype=int)
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char == '.':
            data[i,j] = 0
        else:
            data[i,j] = 1    
# Pad array to give map room to expand
data = np.pad(data,(51,51))

kernel = 2**np.arange(9).reshape(3,3)
print(data)
for step in range(5):
    data = algorithm[convolve(data,kernel)]
    if step+1 in (2,50): print(data.sum())

