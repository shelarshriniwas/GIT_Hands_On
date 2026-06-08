import json

with open("students.json", "r") as file:

    data = json.load(file)

student_id = input("Enter Student ID : ")

if student_id in data:

    new_marks = input("Enter New Marks : ")

    data[student_id]["marks"] = new_marks

with open("students.json", "w") as file:

    json.dump(data, file, indent=4)

print("JSON Data Updated")