import copy

with open('../data/passage_pathing') as f:
    lines = f.read().splitlines()
path_data = [line.split('-') for line in lines]

#Create path dictionary specifying node connections
path_dict = {}
for path in path_data:
    # Two way dict
    if path[0] not in path_dict:
        path_dict[path[0]] = [path[1]]
    else:
        path_dict[path[0]] += [path[1]]
        
    if path[1] not in path_dict:
        path_dict[path[1]] = [path[0]]
    else:
        path_dict[path[1]] += [path[0]]

# Remove 'end' as a key, so that there are no valid paths once key is reached
path_dict.pop('end')
# Remove 'start' as a value for any key, so that paths back to start are not included
for path_key in path_dict:
    if 'start' in path_dict[path_key]:
        path_dict[path_key].remove('start')
        
def get_valid_caves(path_dict,current_path,current_cave):
    # Find large caves as well as caves that haven't been visited
    valid_caves = [cave for cave in path_dict[current_cave] if cave not in current_path or cave.isupper()]
    # For part 2: allow for one small cave to be visited more than once
    small_caves = [cave for cave in path_dict[current_cave] if cave in current_path and cave.islower()]
    if [current_path.count(cave) for cave in current_path if cave.islower()].count(2)<1:
        valid_caves += small_caves    
    return valid_caves
path_count = 0

def take_step(path_dict,current_path,current_cave,path_count):
    if current_cave == 'end':
        current_path+=['end']
        return 1        

    current_path += [current_cave]
    next_caves = get_valid_caves(path_dict,current_path,current_cave)

    if not next_caves:
        return 0
        
    return sum([take_step(path_dict,current_path.copy(),next_cave,path_count) for next_cave in next_caves])    
    return path_count

current_path = []
print(take_step(path_dict,current_path,'start',0))