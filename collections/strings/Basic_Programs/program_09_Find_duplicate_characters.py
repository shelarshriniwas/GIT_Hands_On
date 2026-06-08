# program_09_Find_duplicate_characters.py

text = "programming"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

for key, value in frequency.items():

    if value > 1:
        print(key)

# Logic 2

text = "programming"

duplicates = set()

for i in range(len(text)):

    for j in range(i + 1, len(text)):

        if text[i] == text[j]:
            duplicates.add(text[i])

print(duplicates)