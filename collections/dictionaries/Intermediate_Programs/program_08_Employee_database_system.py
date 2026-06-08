# program_08_Employee_database_system.py

employees = {
    101: {
        "name": "Rahul",
        "salary": 50000
    },

    102: {
        "name": "Amit",
        "salary": 60000
    }
}

for emp_id, details in employees.items():
    print(emp_id, details)