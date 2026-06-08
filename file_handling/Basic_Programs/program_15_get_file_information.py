# program_15_get_file_information.py

import os
import time

file_name = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file3.txt"

print("File Size :", os.path.getsize(file_name), "bytes")
print("Created Time :", time.ctime(os.path.getctime(file_name)))
print("Modified Time :", time.ctime(os.path.getmtime(file_name)))