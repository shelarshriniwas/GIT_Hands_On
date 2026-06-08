'''
Input:

folder contains:
a.txt
b.txt
c.txt

Output:

file_1.txt
file_2.txt
file_3.txt

'''

import os

folder_path = "files"   # folder name where files are present

files = os.listdir(folder_path)    # lsit of all files form path 

for index, file in enumerate(files, start=1):
    old_path = os.path.join(folder_path, file)

    extension = os.path.splitext(file)[1]

    new_name = f"file_{index}{extension}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

print("Files Renamed Successfully")