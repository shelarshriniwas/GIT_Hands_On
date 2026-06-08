'''
Input:

{'a':1,'b':2,'c':3}

Output:

{1:'a',2:'b',3:'c'}
'''

data = {'a':1,'b':2,'c':3}

result = {}

for key, value in data.items():
    result[value] = key

print(result)