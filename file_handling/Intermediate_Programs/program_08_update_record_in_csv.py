# program_08_update_record_in_csv.py

import csv

records = []

search_id = input("Enter ID To Update : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if row[0] == search_id:

            row[1] = input("Enter New Name : ")
            row[2] = input("Enter New Marks : ")

        records.append(row)

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(records)

print("Record Updated")