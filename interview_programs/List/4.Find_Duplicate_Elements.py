'''

Input:
[1,2,3,2,4,5,1]
Output:
[1,2]
'''
nums = [1,2,3,2,4,5,1]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))