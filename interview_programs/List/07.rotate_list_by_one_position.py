'''
Input
1 2 3 4 5
Output
5 1 2 3 4
'''

l1 = [1,2,3,4,5]
k = 1

result = [l1[-k]] + l1[:-k]

print(result)

