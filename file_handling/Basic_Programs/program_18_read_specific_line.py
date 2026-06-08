# program_18_read_specific_line.py

import os

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"
n = int(input("Enter the line no which want to read: "))

with open(path2,"r") as f:
    lines = f.readlines()

    if n <= len(lines):
        print(lines[n-1])
    else:
        print("Line Not Found")    

