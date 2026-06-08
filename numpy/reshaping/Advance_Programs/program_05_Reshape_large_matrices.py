#program_05_Reshape_large_matrices.py

import numpy as np

arr = np.arange(1000000)

result = arr.reshape(1000,1000)

print(result.shape)