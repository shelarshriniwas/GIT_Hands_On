#program_05_Pairwise_subtraction.py

import numpy as np

arr = np.array([10,20,30])

result = arr[:,None] - arr

print(result)