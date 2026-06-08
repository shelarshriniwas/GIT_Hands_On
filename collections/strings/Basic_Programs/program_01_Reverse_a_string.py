# program_01_Reverse_a_string.py

s = "This is reverse string program"

print(s[::-1])

text = "Python"

reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)