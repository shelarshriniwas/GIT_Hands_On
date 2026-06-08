#program_01_Sliding_window_extraction.py

import numpy as np

arr = np.array([1,2,3,4,5,6])

window_size = 3

for i in range(len(arr)-window_size+1):
    print(arr[i:i+window_size])