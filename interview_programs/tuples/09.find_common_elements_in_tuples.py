'''
Input
(1,2,3,4)
(3,4,5,6)
Output
(3,4)
'''

t1 = (1,2,3,4)
t2 = (3,4,5,6)

t3 = []

for i in list(t1):
    if i in list(t2):
        t3.append(i)

print(tuple(t3))