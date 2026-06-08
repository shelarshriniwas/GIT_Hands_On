# program_07_search_record_in_csv.py

import csv

search_id = input("Enter ID To Search : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if search_id in row:
            print(row)