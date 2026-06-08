# program_12_write_json_data.py

import json

student = {
    "id": 101,
    "name": "Shri",
    "marks": 85
}

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)

print("JSON Data Written")