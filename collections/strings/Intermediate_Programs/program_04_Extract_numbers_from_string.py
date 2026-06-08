# program_04_Extract_numbers_from_string.py

text = "Python123AWS456"

numbers = ""

for char in text:

    if char.isdigit():
        numbers += char

print(numbers)