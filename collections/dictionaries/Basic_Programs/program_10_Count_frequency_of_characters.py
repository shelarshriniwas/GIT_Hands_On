# program_10_Count_frequency_of_characters.py

text = "python"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print(frequency)