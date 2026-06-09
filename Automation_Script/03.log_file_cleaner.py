'''
Input
error.log
server.log
notes.txt
Output
notes.txt
'''

import os

path = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation_Script\\Automation Files"

for file in os.listdir(path):
    if file.endswith(".log"):
        os.remove(os.path.join(path, file))

print("Log files deleted")