# program_02_Parent-child_class.py

class Parent:

    def home(self):

        print("Parent Owns Home")


class Child(Parent):

    def room(self):

        print("Child Has Own Room")


obj = Child()

obj.home()
obj.room()