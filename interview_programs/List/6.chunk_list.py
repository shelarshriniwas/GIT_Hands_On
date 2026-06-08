'''
Input
List = [1,2,3,4,5,6,7,8]
Chunk Size = 3
Output
[[1,2,3],[4,5,6],[7,8]]
'''

lst = [1,2,3,4,5,6,7,8,9,10]

size = 3

result = []

for i in range(0, len(lst), size):
    result.append(lst[i:i+size])

print(result)