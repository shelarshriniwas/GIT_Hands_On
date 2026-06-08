#program_09_Alternate_column_slicing.py

import numpy as np

arr = np.arange(1,17).reshape(4,4)

print(arr[:,::2])