# program_15_convert_json_to_dictionary.py

import json

student = {
    "name": "Shri",
    "course": "Python"
}

json_data = json.dumps(student, indent=4)

print(json_data)