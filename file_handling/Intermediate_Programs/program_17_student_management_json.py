# program_17_student_management_json.py

import json

students = {}

student_id = input("Enter Student ID : ")
name = input("Enter Name : ")
marks = input("Enter Marks : ")

students[student_id] = {
    "name": name,
    "marks": marks
}

with open("students.json", "w") as file:

    json.dump(students, file, indent=4)

print("Student Data Stored")