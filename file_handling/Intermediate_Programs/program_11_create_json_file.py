# program_11_create_json_file.py

import json

data = {}

with open("data.json", "w") as file:

    json.dump(data, file)

print("JSON File Created")