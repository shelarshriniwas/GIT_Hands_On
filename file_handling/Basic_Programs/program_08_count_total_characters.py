# program_08_count_total_characters.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"


with open(path2,"r") as f1:
    data = f1.read()

print("Total Characters in file: ",len(data))