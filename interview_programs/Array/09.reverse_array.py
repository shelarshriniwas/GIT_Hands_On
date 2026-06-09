'''
Input
1 2 3 4 5
Output
5 4 3 2 1
'''

arr = [1,2,3,4,5]
rev = []

arr.reverse()
print("Using Reverse() : ",arr)


for i in range(len(arr),0,-1):
    rev.append(i)

print("Using for loop : ",rev)
