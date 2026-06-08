# program_10_Payroll_generator.py

class Employee:

    def __init__(self, name, basic_salary, bonus):
        self.name = name
        self.basic_salary = basic_salary
        self.bonus = bonus

    def salary_slip(self):

        total_salary = self.basic_salary + self.bonus

        print("\n------ SALARY SLIP ------")
        print("Employee Name :", self.name)
        print("Basic Salary :", self.basic_salary)
        print("Bonus :", self.bonus)
        print("Total Salary :", total_salary)


name = input("Enter Employee Name : ")
salary = int(input("Enter Basic Salary : "))
bonus = int(input("Enter Bonus : "))

obj = Employee(name, salary, bonus)

obj.salary_slip()