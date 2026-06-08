# program_28_find_duplicate_words.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

frequency = {}

with open(path2, "r") as file:

    data = file.read().lower()

    words = data.split()

    for word in words:

        frequency[word] = frequency.get(word, 0) + 1

print("Duplicate Words")

for key, value in frequency.items():

    if value > 1:
        print(key, ":", value)