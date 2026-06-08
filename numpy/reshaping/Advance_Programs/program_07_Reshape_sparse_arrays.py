#program_07_Reshape_sparse_arrays.py

import numpy as np

sparse = np.zeros(16)

sparse[2] = 10
sparse[8] = 20

result = sparse.reshape(4,4)

print(result)