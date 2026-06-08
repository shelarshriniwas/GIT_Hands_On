# List all files from a folder.

import os

folder_path = input("Enter Folder Path : ")

files = os.listdir(folder_path)

print("Files And Folders")

for file in files:
    print(file)