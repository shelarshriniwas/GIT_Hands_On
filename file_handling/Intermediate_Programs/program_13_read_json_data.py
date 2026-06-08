# program_13_read_json_data.py

import json

with open("student.json", "r") as file:

    data = json.load(file)

print(data)