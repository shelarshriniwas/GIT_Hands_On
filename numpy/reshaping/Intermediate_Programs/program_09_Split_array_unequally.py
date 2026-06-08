#program_09_Split_array_unequally.py

import numpy as np

arr = np.arange(10)

parts = np.array_split(arr,3)

for part in parts:
    print(part)