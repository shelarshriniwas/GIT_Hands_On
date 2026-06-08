#program_03_Index_random_positions.py

import numpy as np

arr = np.arange(1,21)

print(arr)

positions = np.random.randint(0,len(arr),5)

print(arr[positions])