#program_04_Normalize_array.py

import numpy as np

arr = np.array([10,20,30,40,50])

normalized = arr / arr.max()

print(normalized)