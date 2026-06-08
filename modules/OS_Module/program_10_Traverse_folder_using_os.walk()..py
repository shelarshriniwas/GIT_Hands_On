# Traverse folder using os.walk().
import os

path = input("Enter Folder Path : ")

for root, folders, files in os.walk(path):

    print("\nCurrent Path :", root)

    print("Folders")
    for folder in folders:
        print(folder)

    print("Files")
    for file in files:
        print(file)