'''
Input:
[1, 2,0,0, 3, 5]
Output:
[1, 2, 3, 5, 0, 0]

'''
n = int(input("Enter the no of elements want to add in arr: "))
nums = []

for i in range(n):
    nums.append(int(input()))

print("Array Elements: ",nums)

j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print(nums)