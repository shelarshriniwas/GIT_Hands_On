# program_06_Remove_spaces_from_string.py

text = "Python AWS"

result = ""

for char in text:

    if char != " ":
        result += char

print(result)