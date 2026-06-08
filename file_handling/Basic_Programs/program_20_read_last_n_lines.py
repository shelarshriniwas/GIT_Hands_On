# program_20_read_last_n_lines.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

n = int(input("Enter the line no which want to read: "))

with open(path2, "r") as file:

    lines = file.readlines()

    for line in lines[-n:]:
        print(line, end="")