#program_08_Complex_Boolean_indexing.py

import numpy as np

arr = np.array([10,25,40,55,70,85])

result = arr[(arr > 30) & (arr < 80)]

print(result)