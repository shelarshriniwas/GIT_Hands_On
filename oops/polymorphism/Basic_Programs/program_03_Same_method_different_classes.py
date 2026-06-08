# program_03_Same_method_different_classes.py

class Cat:

    def sound(self):

        print("Cat Meows")


class Dog:

    def sound(self):

        print("Dog Barks")


c = Cat()
d = Dog()

# Same method name
c.sound()
d.sound()