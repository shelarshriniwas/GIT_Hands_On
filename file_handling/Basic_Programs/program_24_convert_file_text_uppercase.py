# program_24_convert_file_text_uppercase.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2, "r") as file:
    data = file.read()

data = data.upper()

with open(path2, "w") as file:
    file.write(data)

print("Converted To Uppercase")