import csv

search_id = input("Enter Student ID : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if row[0] == search_id:

            print("Record Found")
            print(row)