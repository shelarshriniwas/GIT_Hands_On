#program_03_Expand_dimensions.py.

import numpy as np

arr = np.array([1,2,3,4])

result = np.expand_dims(arr,axis=0)

print(result)
print(result.shape)