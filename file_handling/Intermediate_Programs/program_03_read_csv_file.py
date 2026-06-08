# program_03_read_csv_file.py

import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)