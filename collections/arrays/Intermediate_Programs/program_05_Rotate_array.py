# program_05_Rotate_array.py

numbers = [1, 2, 3, 4, 5]

rotate = 2

result = numbers[-rotate:] + numbers[:-rotate]

print(result)