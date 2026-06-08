# program_07_Data_validation_project.py

class Age:

    def __init__(self):

        self.__age = 0

    def set_age(self, age):

        if age > 0:

            self.__age = age

    def display(self):

        print("Age :", self.__age)


obj = Age()

obj.set_age(25)

obj.display()