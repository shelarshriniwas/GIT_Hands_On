# program_04_Find_missing_number_in_array.py

numbers = [1, 2, 3, 5]

n = 5

missing = n * (n + 1) // 2 - sum(numbers)

print(missing)