#program_07_Extract_matrix_quadrants.py

import numpy as np

arr = np.arange(1,17).reshape(4,4)

mid = arr.shape[0] // 2

print("Top Left")
print(arr[:mid,:mid])

print("Top Right")
print(arr[:mid,mid:])

print("Bottom Left")
print(arr[mid:,:mid])

print("Bottom Right")
print(arr[mid:,mid:])