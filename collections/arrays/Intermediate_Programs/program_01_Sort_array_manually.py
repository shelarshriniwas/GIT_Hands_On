# program_01_Sort_array_manually.py

from array import *

numbers = array('i', [50, 20, 10, 40])

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)