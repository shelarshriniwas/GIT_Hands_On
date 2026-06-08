# program_10_sort_csv_records.py

import csv

with open("students.csv", "r") as file:

    reader = list(csv.reader(file))

header = reader[0]
data = reader[1:]

data.sort()

with open("sorted_students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(data)

print("Records Sorted")