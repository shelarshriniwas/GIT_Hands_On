import json

student = {
    "id": 101,
    "name": "Shri",
    "marks": 90
}

json_data = json.dumps(student, indent=4)

print(json_data)