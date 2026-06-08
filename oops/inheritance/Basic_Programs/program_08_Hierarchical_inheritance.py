# program_08_Hierarchical_inheritance.py

class Parent:

    def property(self):

        print("Parent Property")


class Son(Parent):

    def bike(self):

        print("Son Has Bike")


class Daughter(Parent):

    def scooty(self):

        print("Daughter Has Scooty")


s = Son()
d = Daughter()

s.property()
s.bike()

d.property()
d.scooty()