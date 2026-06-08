#program_10_Copy_slice_into_new_array.py

import numpy as np

arr = np.arange(1,11)

new_arr = arr[2:7].copy()

print(new_arr)