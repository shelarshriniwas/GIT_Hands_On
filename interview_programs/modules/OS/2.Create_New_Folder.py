'''
Program 2.Create_New_Folder.py
Interview_Practice

Output:

Folder Created
'''

import os

print("Current Working directory : ")
pa = os.getcwd()
print(pa)
new_folder = input("enter new folder name : ")
os.mkdir(new_folder)

print("Please check is folder created in current directory: ")