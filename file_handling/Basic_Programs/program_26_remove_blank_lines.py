# program_26_remove_blank_lines.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2, "r") as file:
    lines = file.readlines()


with open(path2, "w") as file:

    for line in lines:

        if line.strip() != "":
            file.write(line)

print("Blank Lines Removed")