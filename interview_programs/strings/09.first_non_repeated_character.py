'''
Input : swiss
Output: w
'''

s1 = "swiss"

for ch in s1:
    if s1.count(ch) == 1:
        print(ch)
        break
print("First Non Repeated Char : ", ch)