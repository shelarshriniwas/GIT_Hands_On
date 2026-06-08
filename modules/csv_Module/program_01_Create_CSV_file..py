import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    print("CSV File Created")