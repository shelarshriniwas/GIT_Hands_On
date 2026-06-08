# program_28_binary_employee_system.py

import pickle

employee = {}

emp_id = input("Enter Employee ID : ")
name = input("Enter Name : ")
salary = input("Enter Salary : ")

employee[emp_id] = {
    "name": name,
    "salary": salary
}

with open("employee.pkl", "wb") as file:

    pickle.dump(employee, file)

print("Employee Stored")