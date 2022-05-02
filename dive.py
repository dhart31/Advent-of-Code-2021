import pandas as pd

command_table = pd.read_table('../data/submarine_position',names=['direction','magnitude'],delimiter=' ')

# PART 1
horizontal_pos = 0
depth = 0
aim = 0
for index, row in command_table.iterrows():
    direction = row['direction']
    magnitude = row['magnitude']
    if direction == 'forward':
        horizontal_pos += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude        
print(horizontal_pos*depth)

# PART 2
horizontal_pos = 0
depth = 0
aim = 0
for index, row in command_table.iterrows():
    direction = row['direction']
    magnitude = row['magnitude']
    if direction == 'forward':
        horizontal_pos += magnitude
        depth += magnitude*aim
    elif direction == 'down':
        aim += magnitude
    elif direction == 'up':
        aim -= magnitude        
print(horizontal_pos*depth)