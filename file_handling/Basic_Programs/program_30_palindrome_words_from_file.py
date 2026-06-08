# program_30_palindrome_words_from_file.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2, "r") as file:

    data = file.read().lower()

words = data.split()

print("Palindrome Words")

for word in words:

    if word == word[::-1]:
        print(word)