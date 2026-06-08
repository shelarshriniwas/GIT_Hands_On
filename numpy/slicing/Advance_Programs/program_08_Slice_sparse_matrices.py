#program_08_Slice_sparse_matrices.py

import numpy as np

sparse = np.zeros((6,6))

sparse[1,2] = 10
sparse[3,4] = 20

print(sparse[0:4,0:4])