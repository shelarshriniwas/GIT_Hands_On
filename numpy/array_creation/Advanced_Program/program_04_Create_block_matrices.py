# program_04_Create_block_matrices.py

import numpy as np

a = np.ones((2,2))
b = np.zeros((2,2))

block = np.block([
    [a,b],
    [b,a]
])

print(block)