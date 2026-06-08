#program_02_Reshape_2D_to_1D.py

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

result = arr.reshape(6)

print(result)