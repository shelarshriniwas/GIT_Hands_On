'''
Input
{'A':10,'B':20,'C':30}
Output
60
'''

data = {'A':10,'B':20,'C':30}

total = 0

for value in data.values():
    total += value

print(total)