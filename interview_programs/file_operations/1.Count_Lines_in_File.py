'''
Program 1.Count_Lines_in_File.py
sample.txt

Output:

Total Lines = X

'''

with open("f.txt","r") as f:
    data = f.readlines()

print("total lines in file: ",len(data))