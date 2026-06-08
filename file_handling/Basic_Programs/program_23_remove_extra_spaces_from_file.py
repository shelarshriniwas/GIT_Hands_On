# program_23_remove_extra_spaces_from_file.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2, "r") as file:
    data = file.read()

data = " ".join(data.split())

with open(path2, "w") as file:
    file.write(data)

print("Extra Spaces Removed")