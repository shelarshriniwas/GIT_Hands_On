'''
Input
10 50 30 20
Output
50
'''


l1 = [10,50,20,30,40,70]
max_ele = l1[0]

for i in l1:
    if i > max_ele:
        max_ele = i

print("Maximum element is : ",max_ele)

