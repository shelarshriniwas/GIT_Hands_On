#program_08_Split_array_equally.py

import numpy as np

arr = np.arange(12)

parts = np.split(arr,4)

for part in parts:
    print(part)