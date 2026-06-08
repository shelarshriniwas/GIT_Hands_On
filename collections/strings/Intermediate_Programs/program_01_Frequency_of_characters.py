# program_01_Frequency_of_characters.py

s = "This is Frequency of characters"

freq = {}

for i in s.lower():
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq) 