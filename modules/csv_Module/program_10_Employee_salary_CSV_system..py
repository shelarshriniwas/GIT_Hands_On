import csv

with open("employees.csv", "a", newline="") as file:

    writer = csv.writer(file)

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Employee Name : ")
    salary = input("Enter Salary : ")

    writer.writerow([emp_id, name, salary])

print("Employee Salary Stored")