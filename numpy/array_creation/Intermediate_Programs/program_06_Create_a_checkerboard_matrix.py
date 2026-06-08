# program_06_Create_a_checkerboard_matrix.py

import numpy as np

arr = np.zeros((8,8),dtype=int)

arr[1::2,::2] = 1
arr[::2,1::2] = 1

print(arr)