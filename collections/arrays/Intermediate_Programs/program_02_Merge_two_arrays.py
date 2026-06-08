# program_02_Merge_two_arrays.py

from array import *

arr1 = array('i', [1, 2, 3])

arr2 = array('i', [4, 5, 6])

arr1.extend(arr2)

print(arr1)