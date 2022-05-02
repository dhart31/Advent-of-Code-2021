import numpy as np
from scipy import stats
        
def bit2int(bit_array):
    return(int(''.join(str(int(i)) for i in bit_array),2))

def most_common_bit(bit_array):
    counts = np.bincount(bit_array)
    if counts[0]==counts[1]:
        return(1)
    else:
        return np.argmax(counts)

def least_common_bit(bit_array):
    counts = np.bincount(bit_array)
    if counts[0]==counts[1]:
        return(0)
    else:
        return np.argmin(counts)

lines = open('../data/binary_diagnostic').read().splitlines()
binary_diagnostic = np.transpose(np.array([list(map(int,list(line))) for line in lines])) # Convert to int array, transposed for iteration

# PART 1
gamma = bit2int([most_common_bit(row) for row in binary_diagnostic])
epsilon = bit2int([least_common_bit(row) for row in binary_diagnostic])
print(gamma*epsilon)

binary_oxygen = binary_c02 = binary_diagnostic

# PART 2
count = 0
while np.size(binary_oxygen,1) > 1:
    row = binary_oxygen[count,:]
    binary_oxygen = binary_oxygen[:,most_common_bit(row)==row]
    count +=1
oxygen = bit2int(binary_oxygen)
    
count = 0
while np.size(binary_c02,1) > 1:
    row = binary_c02[count,:]
    binary_c02 = binary_c02[:,least_common_bit(row)==row]
    count +=1

c02 = bit2int(binary_c02)

print(oxygen*c02)  
