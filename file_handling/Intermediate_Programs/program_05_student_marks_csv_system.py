# program_05_student_marks_csv_system.py

import csv

with open("marks.csv", "a", newline="") as file:

    writer = csv.writer(file)

    roll = input("Enter Roll Number : ")
    name = input("Enter Name : ")
    marks = float(input("Enter Marks : "))

    writer.writerow([roll, name, marks])

print("Student Record Added")