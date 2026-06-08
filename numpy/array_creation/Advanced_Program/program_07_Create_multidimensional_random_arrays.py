# program_07_Create_multidimensional_random_arrays.py

import numpy as np

arr = np.random.randint(
    1,
    100,
    size=(3,4,5)
)

print(arr)