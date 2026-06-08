# program_02_Method_overriding.py

class Animal:

    def sound(self):

        print("Animal Makes Sound")


class Dog(Animal):

    # Parent method overridden
    def sound(self):

        print("Dog Barks")


obj = Dog()

obj.sound()