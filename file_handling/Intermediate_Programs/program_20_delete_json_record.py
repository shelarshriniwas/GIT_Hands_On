# program_20_delete_json_record.py

import json

with open("students.json", "r") as file:

    data = json.load(file)

student_id = input("Enter Student ID To Delete : ")

if student_id in data:
    del data[student_id]

with open("students.json", "w") as file:

    json.dump(data, file, indent=4)

print("Record Deleted")