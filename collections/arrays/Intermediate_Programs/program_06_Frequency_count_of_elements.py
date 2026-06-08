# program_06_Frequency_count_of_elements.py

numbers = [1, 2, 2, 3, 1, 4]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1

    else:
        frequency[num] = 1

print(frequency)