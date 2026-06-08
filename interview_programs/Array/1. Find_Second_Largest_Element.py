'''
1. Find Second Largest Element: 
i/o = arr = [10, 20, 50, 40, 30]  
o/p: = 40
'''

n = int(input("Enter the no of elements want add in array: "))
arr = []

for i in range(n):
    arr.append(int(input()))

large = second_large = arr[0]

for i in arr:
    if i > large:
        second_large = large
        large = i
    elif i > second_large and i != large:
        second_large = i

print("second_large: ",second_large)   