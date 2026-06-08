# program_01_Private_variables_example.py
class Student:

    def __init__(self):

        # Private variable
        # Double underscore makes variable private
        # Cannot access directly outside class
        self.__name = "Shriniwas"

    def display(self):

        # Accessing private variable inside class
        print("Student Name :", self.__name)


obj = Student()

obj.display()