'''

Program 2: Find_Common_Elements
a = [1,2,3,4]
b = [3,4,5,6]

Output:

[3,4]
'''

a = []
b = []
n = int(input("Enter the no of elements want to add in list: "))

for i in range(n):
    a.append(int(input()))

n1 = int(input("Enter the no of elements want to add in list: "))

for i in range(n1):
    b.append(int(input()))

res = []

for i in a:
    if i in b:
        res.append(i)
    else:
        continue

print("Common Elements: ",res)