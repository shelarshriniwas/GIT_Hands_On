# program_09_Create_memory-efficient_arrays.py

import numpy as np

arr = np.array(
    [1,2,3,4,5],
    dtype=np.uint8
)

print(arr)
print(arr.nbytes)