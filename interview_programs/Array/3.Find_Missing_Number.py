'''
Input:
[1, 2, 3, 5]
Output:
4

'''

n = int(input("Enter the no of elements want to add in arr: "))
arr = []

for i in range(n):
    arr.append(int(input()))

print("Array Elements: ",arr)

expected_sum  = len(arr) * (len(arr)+1) // 2

sum1 = sum(arr)

Missing_number = expected_sum - sum1

print("Missing number is : ",Missing_number)