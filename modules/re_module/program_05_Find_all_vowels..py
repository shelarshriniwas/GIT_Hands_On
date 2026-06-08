import re

text = "Python AWS"

vowels = re.findall(r"[aeiouAEIOU]", text)

print(vowels)

text = "Python AWS"
vowels_set = "aeiouAEIOU"

result = []

for char in text:
    if char in vowels_set:
        result.append(char)

print(result)