#program_05_Dynamic_slicing.py

import numpy as np

arr = np.arange(1,31)

start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

print(arr[start:stop:step])