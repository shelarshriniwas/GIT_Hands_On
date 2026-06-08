#program_06_Pairwise_multiplication.py

import numpy as np

arr = np.array([1,2,3])

result = arr[:,None] * arr

print(result)