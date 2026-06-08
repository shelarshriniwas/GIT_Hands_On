# program_14_get_file_size.py

import os

path3 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file3.txt"

data = os.path.getsize(path3)

print("Total size: ",data)