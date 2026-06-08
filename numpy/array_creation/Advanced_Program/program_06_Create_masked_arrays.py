# program_06_Create_masked_arrays.py

import numpy as np
import numpy.ma as ma

arr = np.array([10,20,30,40,50])

masked = ma.masked_greater(arr,30)

print(masked)