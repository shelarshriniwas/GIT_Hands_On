#program_10_Access_specific_rows_and_columns.py

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr[[0,2], :])