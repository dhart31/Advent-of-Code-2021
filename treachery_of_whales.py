import numpy as np

crab_pos = np.loadtxt('../data/crab_positions',delimiter = ',',dtype=int)
min_pos = np.min(crab_pos)
max_pos = np.max(crab_pos)

# PART 1
costs = np.zeros(max_pos-min_pos+1)
for pos in np.arange(min_pos,max_pos+1):
    costs[pos] = np.sum(np.abs(crab_pos-pos))
min_cost_idx = np.argmin(costs)
print(int(costs[min_cost_idx]))

# PART 2
cost2 = np.zeros(max_pos-min_pos+1)
for pos in np.arange(min_pos,max_pos+1):
    diff = np.abs(crab_pos - pos)
    # 1+2+3+...n = n*(n+1)/2
    cost2[pos] = np.sum(diff*(diff+1)/2)
min_cost_idx = np.argmin(cost2)
print(int(cost2[min_cost_idx]))

