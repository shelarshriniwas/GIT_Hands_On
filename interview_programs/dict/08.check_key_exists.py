'''
Input
Dictionary={'name':'John','age':25}
Key=age
Output
Key Found
'''

data = {'name':'John','age':25}
key = 'age'

for k,v in data.items():
    if k == key:
        print("Key Found")

