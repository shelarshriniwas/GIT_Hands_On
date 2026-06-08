# program_09_Find_repeated_elements.py

numbers = (1, 2, 3, 2, 4, 5, 1)

repeated = set()

for num in numbers:
    if numbers.count(num) > 1:
        repeated.add(num)

print(repeated)