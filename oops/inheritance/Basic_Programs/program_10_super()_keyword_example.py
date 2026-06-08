# program_10_super()_keyword_example.py

class Employee:

    def __init__(self, name):

        self.name = name


class Manager(Employee):

    def __init__(self, name, department):

        # Access parent constructor
        super().__init__(name)

        self.department = department

    def display(self):

        print("Name :", self.name)
        print("Department :", self.department)


obj = Manager("Rahul", "IT")

obj.display()