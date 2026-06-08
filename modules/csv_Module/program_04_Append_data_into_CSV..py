import csv

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    student_id = input("Enter ID : ")
    name = input("Enter Name : ")
    marks = input("Enter Marks : ")

    writer.writerow([student_id, name, marks])

print("Data Appended")