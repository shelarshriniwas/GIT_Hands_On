# program_29_extract_numbers_from_file.py

import os,re

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2, "r") as file:

    data = file.read()

numbers = re.findall(r'\d+', data)

print("Numbers Found")

for num in numbers:
    print(num)