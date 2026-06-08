#program_06_Multi-dimensional_transformations.py

import numpy as np

arr = np.arange(24)

result = arr.reshape(
    2,
    3,
    4
)

print(result)