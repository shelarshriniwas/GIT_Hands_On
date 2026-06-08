#program_10_Verify_reshape_size.py

import numpy as np

arr = np.arange(24)

new_arr = arr.reshape(4,6)

print(arr.size)
print(new_arr.size)