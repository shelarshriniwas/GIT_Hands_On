'''
Input
a.txt
b.txt
c.py
d.py
e.pdf
Output
txt : 2
py  : 2
pdf : 1
'''

import os

path = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation_Script\\Automation Files"

result = {}

for file in os.listdir(path):
    ext = file.split(".")[-1]

    result[ext] = result.get(ext, 0) + 1

for k, v in result.items():
    print(k, ":", v)