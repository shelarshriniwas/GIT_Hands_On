import csv

data = []

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

    for row in reader:

        data.append(row)

data.sort()

print(header)

for row in data:

    print(row)