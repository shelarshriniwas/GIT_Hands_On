'''
Program 1.Copy_File.py
source.txt → backup.txt
'''
 
import shutil

source_file = "source.txt"
destination_file = "backup.txt"

shutil.copy(source_file, destination_file)

print("File copied successfully.")