# program_06_count_total_lines.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"


with open(path2,"r") as f1:
    data = f1.readlines()

print("Total lines in file: ",len(data))