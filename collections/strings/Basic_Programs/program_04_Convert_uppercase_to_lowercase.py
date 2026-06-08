# program_04_Convert_uppercase_to_lowercase.py

text = "PYTHON"

result = ""

for char in text:

    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)

    else:
        result += char

print(result)

# Logic 2

text = "PYTHON AWS"

print(text.lower())