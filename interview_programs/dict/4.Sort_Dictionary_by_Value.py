'''
Input:
{"a": 50, "b": 10, "c": 30}
Output:
{'b': 10, 'c': 30, 'a': 50}
'''

data = {"a": 50, "b": 10, "c": 30}

result = dict(sorted(data.items(), key=lambda item: item[1]))

print(result)