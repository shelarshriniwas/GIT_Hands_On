# program_07_Multilevel_inheritance.py

class GrandFather:

    def land(self):

        print("GrandFather Owns Land")


class Father(GrandFather):

    def house(self):

        print("Father Owns House")


class Son(Father):

    def car(self):

        print("Son Owns Car")


obj = Son()

obj.land()
obj.house()
obj.car()