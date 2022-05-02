import pandas as pd
import numpy as np

# PART 1
depth_vals = pd.Series(np.loadtxt('../data/submarine_depth')) # Get depth values
print(sum(depth_vals.diff()>0)) # Count how often depth value is larger than previous value

# PART 2
depth_vals_slidingwindow = depth_vals.rolling(3).sum() # Sum values in a 3 depth window
print(sum(depth_vals_slidingwindow.diff()>0))
