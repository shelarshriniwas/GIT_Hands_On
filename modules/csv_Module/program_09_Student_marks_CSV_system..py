import csv

with open("marks.csv", "a", newline="") as file:

    writer = csv.writer(file)

    student_id = input("Enter Student ID : ")
    name = input("Enter Name : ")
    marks = int(input("Enter Marks : "))

    writer.writerow([student_id, name, marks])

print("Student Marks Stored")