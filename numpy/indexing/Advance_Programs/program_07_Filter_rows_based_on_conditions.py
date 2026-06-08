#program_07_Filter_rows_based_on_conditions.py

import numpy as np

arr = np.array([
    [10,20],
    [60,70],
    [30,40]
])

print(arr[arr[:,0] > 50])