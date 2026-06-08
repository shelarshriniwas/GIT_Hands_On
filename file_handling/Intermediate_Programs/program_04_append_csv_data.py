# program_04_append_csv_data.py

import csv

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    for i in range(2):

        student_id = input("Enter ID : ")
        name = input("Enter Name : ")
        marks = input("Enter Marks : ")

        writer.writerow([student_id, name, marks])

print("Multiple Records Added")