# program_06_employee_salary_csv_system.py

import csv

with open("employee.csv", "a", newline="") as file:

    writer = csv.writer(file)

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    salary = input("Enter Salary : ")

    writer.writerow([emp_id, name, salary])

print("Employee Record Added")