import numpy as np

def update_counts(counts):
    # Get number of fish whose timers are zero
    num_zeros = counts[0]
    # 0 index counts become 8 index count
    # i index counts become i-1 index count
    counts.append(counts.pop(0))
    # reset timers of zero fish too
    counts[6] += num_zeros
    return counts

def initialize_counts(fish_list):
    num_fish = len(fish_list)
    counts = [0]*9
    for i in range(1,7):
        # Get number of fish for each count, ranging from 1 to 6
        counts[i] = fish_list.count(i)
    return counts
        
with open('../data/lanternfish') as f:
    line = f.readline()
    fish_list = list(map(int,line.split(',')))

counts = initialize_counts(fish_list)

for i in range(256):
    counts = update_counts(counts)
    if i in [80-1,256-1]:
        print(sum(counts))

