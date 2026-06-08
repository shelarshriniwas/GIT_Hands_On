# program_09_copy_data_from_one_file_to_another.py

path1 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file1.txt"
path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

with open(path1,"r")as f1:
    data = f1.read()

with open(path2,"a") as f2:
    f2.write(data)
