# program_10_Create_array_from_user_input.py

import numpy as np

numbers = list(map(int,input("Enter numbers: ").split()))

arr = np.array(numbers)

print(arr)