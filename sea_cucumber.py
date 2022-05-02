with open("../data/sea_cucumber") as f:
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]
    
w = len(lines[0])
h = len(lines)

  
num_steps = 0  
while True:
    num_moves = 0
    locs = []
    for i in range(h):
        for j in range(w):
            if lines[i][j] == '>' and lines[i][(j+1)%w] == '.':
                locs.append((i,j))
                
    for i,j in locs:
        lines[i][j] = '.'
        lines[i][(j+1)%w] = '>'
    num_moves += len(locs)
    
    locs = []
    for i in range(h):
        for j in range(w):
            if lines[i][j] == 'v' and lines[(i+1)%h][j] == '.':
                locs.append((i,j))
                
    for i,j in locs:
        lines[i][j] = '.'
        lines[(i+1)%h][j] = 'v'
    num_moves += len(locs)    
    
    num_steps += 1
    if num_moves == 0:
        break

    
print(num_steps)
