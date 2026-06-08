import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])

    writer.writerow([101, "Shri", 90])

    writer.writerow([102, "Ram", 85])

print("Data Written Successfully")