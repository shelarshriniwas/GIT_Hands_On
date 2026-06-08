#program_07_Extract_border_elements.py

import numpy as np

arr = np.arange(1,26).reshape(5,5)

print("Top Row")
print(arr[0,:])

print("Bottom Row")
print(arr[-1,:])

print("Left Column")
print(arr[:,0])

print("Right Column")
print(arr[:,-1])