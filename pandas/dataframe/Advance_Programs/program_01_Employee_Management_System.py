#program_01_Employee_Management_System.py
import pandas as pd

employees = pd.DataFrame({
    "EmpID":[101,102,103],
    "Name":["John","Sam","David"],
    "Salary":[50000,60000,70000]
})

print(employees)

# Add Employee
employees.loc[len(employees)] = [
    104,
    "Mike",
    80000
]

print(employees)