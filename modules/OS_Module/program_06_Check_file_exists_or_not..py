# Check file exists or not.

import os

file_name = input("Enter File Name : ")

if os.path.exists(file_name):
    print("File Exists")
else:
    print("File Does Not Exist")