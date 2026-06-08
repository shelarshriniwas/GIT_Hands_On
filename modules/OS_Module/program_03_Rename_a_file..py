# Rename a file.

import os

old_name = input("Enter Old File Name : ")
new_name = input("Enter New File Name : ")

os.rename(old_name, new_name)

print("File Renamed Successfully")