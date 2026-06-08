# program_07_Split_array_into_even_and_odd.py

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)

print("Even :", even)
print("Odd :", odd)