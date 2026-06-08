# program_19_read_first_n_lines.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

n = int(input("Enter the line no which want to read: "))

with open(path2, "r") as f:

    for i in range(n):
        print(f.readline(), end="")