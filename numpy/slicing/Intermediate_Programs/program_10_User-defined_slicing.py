#program_10_User-defined_slicing.py

import numpy as np

arr = np.arange(1,21)

start = int(input("Start Index: "))
stop = int(input("Stop Index: "))

print(arr[start:stop])