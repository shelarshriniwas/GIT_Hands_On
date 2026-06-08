import re

text = "Py@th#on$123!"

clean = re.sub(r"[^a-zA-Z0-9]", "", text)

print(clean)

text = "Py@th#on$123!"

result = ""

for char in text:
    if char.isalnum():
        result += char

print(result)