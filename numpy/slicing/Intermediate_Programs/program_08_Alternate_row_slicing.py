#program_08_Alternate_row_slicing.py

import numpy as np

arr = np.arange(1,17).reshape(4,4)

print(arr[::2,:])