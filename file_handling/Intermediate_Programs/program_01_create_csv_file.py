# program_01_create_csv_file.py

import csv

file_name = "students.csv"

with open(file_name, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])

print("CSV File Created")