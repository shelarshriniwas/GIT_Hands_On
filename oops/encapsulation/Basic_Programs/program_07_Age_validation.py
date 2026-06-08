# program_07_Age_validation.py

class Person:

    def __init__(self):

        self.__age = 0

    def set_age(self, age):

        # Validation added
        if age >= 18:

            self.__age = age

        else:

            print("Age must be 18 or above")

    def display(self):

        print("Age :", self.__age)


obj = Person()

obj.set_age(22)

obj.display()