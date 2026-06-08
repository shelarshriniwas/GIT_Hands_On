'''
Input:
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}
Output:
{'a': 10, 'b': 30, 'c': 40}
'''

dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}

after_merge = dict1 | dict2

print(after_merge)