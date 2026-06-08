# program_17_create_folder_and_file.py

import os

folder_name = input("Enter Folder Name : ")

os.mkdir(folder_name)

file_name = input("Enter File Name : ")

path = os.path.join(folder_name, file_name)

with open(path, "w") as file:
    file.write("Hello")

print("Folder and File Created")