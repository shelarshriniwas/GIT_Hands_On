#program_07_Replace_selected_values.py

import numpy as np

arr = np.array([10,60,20,80,30])

arr[arr > 50] = 0

print(arr)