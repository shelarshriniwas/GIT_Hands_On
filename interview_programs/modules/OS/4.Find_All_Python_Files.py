'''
Input:

Current Directory

Output:

app.py
test.py
main.py

'''

import os

files = os.listdir()

for file in files:
    if os.path.isfile(file):
        print(file)