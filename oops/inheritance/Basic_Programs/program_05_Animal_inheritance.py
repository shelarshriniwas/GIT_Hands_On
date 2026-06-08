# program_05_Animal_inheritance.py

class Animal:

    def sound(self):

        print("Animal Makes Sound")


class Cat(Animal):

    def meow(self):

        print("Cat Says Meow")


obj = Cat()

obj.sound()
obj.meow()