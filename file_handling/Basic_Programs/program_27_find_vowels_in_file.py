# program_27_find_vowels_in_file.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

vowels = "aeiouAEIOU"

count = 0

with open(path2, "r") as file:

    data = file.read()

    for char in data:

        if char in vowels:
            count += 1

print("Total Vowels :", count)