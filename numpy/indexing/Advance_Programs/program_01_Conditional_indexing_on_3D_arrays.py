#program_01_Conditional_indexing_on_3D_arrays.py

import numpy as np

arr = np.random.randint(1,100,(2,3,3))

print(arr[arr > 50])