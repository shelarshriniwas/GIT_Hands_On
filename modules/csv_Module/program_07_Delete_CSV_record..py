import csv

new_data = []

delete_id = input("Enter Student ID To Delete : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if row[0] != delete_id:

            new_data.append(row)

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(new_data)

print("Record Deleted")