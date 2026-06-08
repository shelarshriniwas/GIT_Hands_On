# program_09_delete_record_from_csv.py

import csv

records = []

search_id = input("Enter ID To Delete : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if row[0] != search_id:
            records.append(row)

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(records)

print("Record Deleted")