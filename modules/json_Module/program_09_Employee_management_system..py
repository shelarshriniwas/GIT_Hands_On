import json

employees = {}

emp_id = input("Enter Employee ID : ")
name = input("Enter Name : ")
salary = input("Enter Salary : ")

employees[emp_id] = {
    "name": name,
    "salary": salary
}

with open("employees.json", "w") as file:

    json.dump(employees, file, indent=4)

print("Employee Data Stored")