'''
Input
[1,2,3,4]
[3,4,5,6]
Output
[3,4]
'''

l1 = [1,2,3,4]
l2 = [3,4,5,6]
res = []

for i in l1:
    if i in l2:
        res.append(i)

print("Common elements are : ",res)
