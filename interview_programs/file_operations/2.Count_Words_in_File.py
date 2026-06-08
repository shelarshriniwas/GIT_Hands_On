'''
Program 2.Count_Words_in_File.py

Output:

Total Words = X
'''

with open("f.txt","r") as f:
    data = f.read().split()

print(len(data))