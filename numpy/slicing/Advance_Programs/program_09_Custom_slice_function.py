#program_09_Custom_slice_function.py

import numpy as np

def custom_slice(arr,start,end):
    return arr[start:end]

arr = np.arange(1,21)

print(custom_slice(arr,5,10))