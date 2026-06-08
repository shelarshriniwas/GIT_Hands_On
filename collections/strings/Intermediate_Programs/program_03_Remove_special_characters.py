# program_03_Remove_special_characters.py

text = "Python@123#AWS!"

result = ""

for char in text:

    if char.isalnum():
        result += char

print(result)

import re

text = "Python@123#AWS!"

result = re.sub(r'[^a-zA-Z0-9]', '', text)

print(result)