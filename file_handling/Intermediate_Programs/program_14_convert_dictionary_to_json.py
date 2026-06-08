# program_14_convert_dictionary_to_json.py

import json

student = {
    "name": "Shri",
    "course": "Python"
}

json_data = json.dumps(student, indent=4)

print(json_data)