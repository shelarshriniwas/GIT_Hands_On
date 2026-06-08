'''
Input:
[1,2,2,3,3,4,5]
Output:
{1,2,3,4,5}
'''

n = int(input("Enter no of elements want to add: "))
l1 = []
for i in range(n):
   l1.append(int(input()))

print("List elements are: ",l1)

result = set(l1)

print(result)

