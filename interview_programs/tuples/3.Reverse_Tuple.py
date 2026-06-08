'''
Input:

(1,2,3,4,5)

Output:

(5,4,3,2,1)

'''

t1 = (1,2,3,4,5)

t2 = tuple(list(t1[::-1]))

print(t2)