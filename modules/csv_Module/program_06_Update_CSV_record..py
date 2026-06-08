import csv

updated_data = []

search_id = input("Enter Student ID To Update : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if row[0] == search_id:

            row[1] = input("Enter New Name : ")
            row[2] = input("Enter New Marks : ")

        updated_data.append(row)

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(updated_data)

print("Record Updated")