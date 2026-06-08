'''
Program 1: Remove_Duplicates
lst = [1,2,2,3,4,4,5]

Output:

[1,2,3,4,5]
'''

l = []
n = int(input("Enter the no of elements want to add in list: "))

for i in range(n):
    l.append(int(input()))

res = []

for i in l:
    if i not in res:
        res.append(i)
    else:
        continue

print("After remove duplicates: ",res)