'''
Program 2.Move_File.py
file1.txt → new_folder/
'''

import shutil
import os

source_file = "file1.txt"
destination_folder = "new_folder"

# Create folder if not exists
os.makedirs(destination_folder, exist_ok=True)

# Move file
shutil.move(source_file, destination_folder)

print("File moved successfully.")