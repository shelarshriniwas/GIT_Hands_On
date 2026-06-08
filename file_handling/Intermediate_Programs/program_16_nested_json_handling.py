# program_16_nested_json_handling.py

import json

student = {
    "101": {
        "name": "Shri",
        "marks": 90
    }
}

with open("nested.json", "w") as file:

    json.dump(student, file, indent=4)

print("Nested JSON Created")