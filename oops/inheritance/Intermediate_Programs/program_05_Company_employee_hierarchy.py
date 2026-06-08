# program_05_Company_employee_hierarchy.py

class Employee:

    def salary(self):

        print("Salary : 50000")


class Manager(Employee):

    # Inheriting Employee class
    def department(self):

        print("Department : IT")


obj = Manager()

obj.salary()
obj.department()