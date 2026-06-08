# program_05_Employee_constructor.py

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

obj = Employee("Rahul", 90000)

print(obj.name)
print(obj.salary)