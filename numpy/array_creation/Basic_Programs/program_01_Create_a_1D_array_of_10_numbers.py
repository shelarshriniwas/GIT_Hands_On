# program_01_Create_a_1D_array_of_10_numbers.py

import numpy as np

arr = np.array([1,2,3,4,5])

arr1 =([])
print(arr)

n = int(input("Enter the no of elements want to store in array: "))

for i in range(n):
    arr1.append(int(input()))

print(arr1)