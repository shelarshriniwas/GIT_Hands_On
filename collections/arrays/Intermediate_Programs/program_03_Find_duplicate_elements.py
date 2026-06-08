# program_03_Find_duplicate_elements.py

from array import *

numbers = array('i', [1, 2, 3, 2, 4, 1])

duplicates = set()

for num in numbers:
    if numbers.tolist().count(num) > 1:
        duplicates.add(num)

print(duplicates)