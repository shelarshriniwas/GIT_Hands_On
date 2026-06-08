'''
Input:

[2,2,1,1,2,2,2]

Output:

2
'''
nums = [2, 2, 1, 1, 2, 2, 2]

for num in nums:
    if nums.count(num) > len(nums) // 2:
        print(num)
        break