#program_09_Conditional_broadcasting.py

import numpy as np

arr = np.array([10,20,30,40,50])

result = np.where(arr > 25,
                  arr + 100,
                  arr)

print(result)