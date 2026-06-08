# program_19_update_json_data.py

import json

with open("students.json", "r") as file:

    data = json.load(file)

student_id = input("Enter Student ID : ")

if student_id in data:

    data[student_id]["marks"] = input("Enter New Marks : ")

with open("students.json", "w") as file:

    json.dump(data, file, indent=4)

print("JSON Updated")