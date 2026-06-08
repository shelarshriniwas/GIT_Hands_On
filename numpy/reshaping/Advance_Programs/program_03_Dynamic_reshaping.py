#program_03_Dynamic_reshaping.py

import numpy as np

arr = np.arange(24)

rows = int(input("Rows: "))

result = arr.reshape(rows,-1)

print(result)