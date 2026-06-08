# program_21_search_word_in_file.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"
word = input("Enter word to search in file: ")

with open(path2, "r") as f:

    data = f.read()
    

if word in data:
    print("Word Found")
else:
    print("Word Not Found")