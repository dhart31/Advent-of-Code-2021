import math
import numpy as np
import ast
import itertools

def convert_number_to_array(number):
    number = str(number).replace(" ","")
    curr_depth = 0
    number_array = []
    i = 0
    # Create 1D array of number, depth pairs
    while i < len(number)-1:
        # Encountering a left bracket increases depth by 1
        if number[i] == '[':
            curr_depth += 1
            i +=1
        # A right bracket decreases depth by 1
        elif number[i] == ']':
            curr_depth -= 1
            i +=1
        elif number[i] == ',':
            i +=1
        # Numbers are saved with the current depth at any position
        else:
            num_str = ""
            while number[i].isdigit():
                num_str += number[i]
                i+=1
            number_array += [[int(num_str),curr_depth]]
    return number_array

def reduce_array(number_array):
    explode_idx = np.where([pair[1]>4 for pair in number_array])[0]
    split_idx = np.where([pair[0]>=10 for pair in number_array])[0]
    # First check if any numbers should explode (more than 4 levels deep)
    if np.any(explode_idx):
        i = explode_idx[0]
        if number_array[i][1] > 4:
            if i > 0:
                number_array[i-1][0] += number_array[i][0]
            if i < len(number_array)-2:
                number_array[i+2][0] += number_array[i+1][0]
            number_array.pop(i)
            number_array[i][0] = 0
            number_array[i][1] -= 1
            return reduce_array(number_array) 
    # Only after explosions, check for splits (numbers higher than 10)
    if np.any(split_idx):
        i = split_idx[0]
        num = number_array[i][0]
        if num >= 10:
            number_array[i][0] = math.floor(num/2)
            number_array[i][1] += 1
            number_array.insert(i+1,[math.ceil(num/2),number_array[i][1]])
            return reduce_array(number_array)
    else:     
        return number_array
    
def calculate_magnitude(number):
    i = 0
    while i <= len(number)-2:
        # For any number pair encountered with the same depth [i,j], perform 3*i+2*j
        # Then, replace pair with that new value (3*i+2*j)
        # Keep doing this until the whole number is calculated
        if number[i][1] == number[i+1][1]:
            new_val = number[i][0]*3 + number[i+1][0]*2
            new_depth = number[i][1]- 1
            number.pop(i)
            number[i] = [new_val,new_depth]
            i = 0
        else:
            i += 1
    return number[0][0]

# PART 1

# with open("../data/snailfish") as f:
    # lines = f.read().splitlines()
    # num = ast.literal_eval(lines[0])
    # num_array = convert_number_to_array(num)
    # for line in lines[1:]:
        # temp_num = ast.literal_eval(line)
        # num_array += convert_number_to_array(temp_num)
        # num_array = [[val[0],val[1]+1] for val in num_array]
        # num_array = reduce_array(num_array)
#print(calculate_magnitude(num_array))
    
# PART 2

with open("../data/snailfish") as f:
    lines = f.read().splitlines()
    numbers = [convert_number_to_array(ast.literal_eval(line)) for line in lines]
    
# Generate all possible pairs of numbers, using the number, depth form given above 
combos = list(itertools.permutations(numbers,2))

max_magnitude = 0
for num1,num2 in combos:
    num_sum = num1+num2
    num_sum = [[val[0],val[1]+1] for val in num_sum]
    num_array = reduce_array(num_sum)
    magnitude = calculate_magnitude(num_array)
    if magnitude > max_magnitude:
        max_magnitude = magnitude
        
        
print(max_magnitude)
#num_array = convert_number_to_array(number)
#print(reduce_array(num_array))
        