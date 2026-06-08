# program_26_student_object_storage.py

import pickle

students = []

name = input("Enter Name : ")
marks = input("Enter Marks : ")

students.append({
    "name": name,
    "marks": marks
})

with open("students.pkl", "wb") as file:

    pickle.dump(students, file)

print("Student Object Stored")