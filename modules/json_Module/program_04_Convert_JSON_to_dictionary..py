import json

json_data = '''
{
    "id": 101,
    "name": "Shri",
    "marks": 90
}
'''

dictionary = json.loads(json_data)

print(dictionary)