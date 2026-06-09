'''
Input
abc.txt
test.txt
demo.txt
Output
file_1.txt
file_2.txt
file_3.txt

'''

import os

path = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation_Script\\Automation Files"

files = os.listdir(path)

count = 1

for file in files:
    if file.endswith(".txt"):
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, f"file_{count}.txt")

        os.rename(old_path, new_path)
        count += 1

print("Renamed Successfully")