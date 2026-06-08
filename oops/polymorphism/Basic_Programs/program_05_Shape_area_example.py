# program_05_Shape_area_example.py

class Circle:

    def area(self):

        radius = 5

        print("Circle Area :", 3.14 * radius * radius)


class Square:

    def area(self):

        side = 4

        print("Square Area :", side * side)


c = Circle()
s = Square()

c.area()
s.area()