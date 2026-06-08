# program_05_read_file_line_by_line.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

# print only one line:

with open(path2,"r") as f:
    print("\n ",f.readline())

with open(path2,"r") as f1:
    data = f1.readlines()

for line in data:
    print(line)