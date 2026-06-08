# program_03_Employee_inheritance.py

class Employee:

    def employee_info(self):

        print("Employee Details")


class Manager(Employee):

    def manager_info(self):

        print("Manager Department")


obj = Manager()

obj.employee_info()
obj.manager_info()