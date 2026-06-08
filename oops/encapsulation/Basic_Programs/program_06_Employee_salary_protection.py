# program_06_Employee_salary_protection.py

class Employee:

    def __init__(self):

        self.__salary = 0

    def set_salary(self, salary):

        if salary > 0:

            self.__salary = salary

    def display(self):

        print("Salary :", self.__salary)


obj = Employee()

obj.set_salary(50000)

obj.display()