# program_04_append_data_into_file.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path2,"r") as f:
    print("\n ",f.read())


with open(path2,"a") as f1:
    f1.write("\n This is append data program - 4")
    
with open(path2,"r") as f2:
    print(f2.read())


