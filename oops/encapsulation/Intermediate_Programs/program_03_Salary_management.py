# program_03_Salary_management.py

class Employee:

    def __init__(self):

        self.__salary = 0

    def set_salary(self, salary):

        # Validation before assigning salary
        if salary > 0:

            self.__salary = salary

    def get_salary(self):

        return self.__salary


obj = Employee()

obj.set_salary(50000)

print("Salary :", obj.get_salary())