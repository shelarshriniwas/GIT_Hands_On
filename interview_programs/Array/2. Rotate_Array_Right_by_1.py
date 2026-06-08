'''
Program 2: Rotate Array Right by 1
arr = [1, 2, 3, 4, 5]
Output:
[5, 1, 2, 3, 4]

'''

n = int(input("Enter the no of elements want add in array: "))
arr = []
res = []
for i in range(n):
    arr.append(int(input()))
print("Array is : ",arr)

r = int(input("Enter the rotate number: "))

res = arr[-r:] + arr[:-r]

print("After rotate array by right : ",res)
