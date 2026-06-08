# program_10_merge_two_text_files.py

path1 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file1.txt"
path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"
path4 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file4.txt"

with open(path1,"r")as f1:
    data = f1.read()

with open(path2,"r") as f2:
    data1 = f2.read()

with open(path4,"a") as f4:
    f4.write(data+data1)