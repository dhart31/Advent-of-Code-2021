import cProfile
import pstats
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

import numpy as np

with open('../data/chiton') as f:
    lines = f.read().splitlines()
    lines = [[int(i) for i in list(line)] for line in lines]

data = np.array(lines)
data = np.concatenate([data]+[(data+i)%9+1 for i in range(4)],1) #Copy cave tile rightward, incrementing by 1 each block
data = np.concatenate([data]+[(data+i)%9+1 for i in range(4)],0) # Now copy tiles downward, incrementing again

num_rows = np.size(data,0)
num_cols = np.size(data,1)


def indices_array(m,n):
    r0 = np.arange(m)
    r1 = np.arange(n)
    out = np.empty((m,n,2),dtype=int)
    out[:,:,0] = r0[:,None]
    out[:,:,1] = r1
    return out

def get_neighbors(num_rows,num_cols,u):
    y = u[0]
    x = u[1]
    
    if y < num_rows-1:
        yield [y+1,x]
    if y > 0:
        yield [y-1,x]
    if x < num_cols-1:
        yield [y,x+1]
    if x > 0:
        yield [y,x-1]
        

# DIJKSTRAS ALGORITHM

dist = np.ones((num_rows,num_cols))*np.inf
prev = [[[None,None]]*num_cols for i in range(num_rows)]
Q = np.ones((num_rows,num_cols),dtype=bool)
idx_array = indices_array(num_rows,num_cols)
dist[0,0] = 0

while Q.any():
    min_dist = np.inf
    idxs = idx_array[Q]
    for idx in idxs:
        if dist[idx[0],idx[1]] < min_dist:
            min_dist = dist[idx[0],idx[1]]
            u = [idx[0],idx[1]]
    Q[u[0],u[1]] = 0
    for v in get_neighbors(num_rows,num_cols,u):
        if Q[v[0],v[1]]:
            alt = dist[u[0],u[1]] + data[v[0],v[1]]
            if alt < dist[v[0],v[1]]:
                dist[v[0],v[1]] = alt
                prev[v[0]][v[1]] = u

u = [9,9]
S = []
print(prev[9][9])

while u != [None,None]:
    S.insert(0,u)
    u = prev[u[0]][u[1]]

#print(S)
print(dist[num_rows-1,num_cols-1])
    