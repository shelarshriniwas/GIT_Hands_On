# program_06_Shape_area_calculator.py

class Shape:

    def formula(self):

        print("Using Area Formula")


class Circle(Shape):

    def area(self):

        radius = 5

        print("Circle Area :", 3.14 * radius * radius)


obj = Circle()

obj.formula()
obj.area()