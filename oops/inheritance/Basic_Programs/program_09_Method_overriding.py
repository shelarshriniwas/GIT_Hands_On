# program_09_Method_overriding.py

class Animal:

    def sound(self):

        print("Animal Makes Sound")


class Dog(Animal):

    # Overriding parent method
    def sound(self):

        print("Dog Barks")


obj = Dog()

obj.sound()