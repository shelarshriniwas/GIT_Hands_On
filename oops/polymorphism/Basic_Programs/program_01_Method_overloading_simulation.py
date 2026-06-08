# program_01_Method_overloading_simulation.py

class Calculator:

    # Default arguments used
    # Python does not support true method overloading
    def add(self, a, b=0, c=0):

        print("Addition :", a + b + c)


obj = Calculator()

obj.add(10, 20)

obj.add(10, 20, 30)


class Display:

    def show(self, name=None):

        # Different behavior based on parameter
        if name is None:

            print("Welcome User")

        else:

            print("Welcome", name)


obj = Display()

obj.show()

obj.show("Shriniwas")