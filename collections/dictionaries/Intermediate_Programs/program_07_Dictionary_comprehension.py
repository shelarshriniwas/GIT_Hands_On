# program_07_Dictionary_comprehension.py

numbers = [1, 2, 3, 4, 5]

square = {
    num: num ** 2 for num in numbers
}

print(square)