'''
Input
45 12 78 9 34
Output
9
'''

arr = [60, 80, 90, 50, 20, 5, 30, 40, 50]

small = arr[0]

for i in arr:
    if i < small:
        small = i
    
print(small)