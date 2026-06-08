# program_02_Abstract_method_implementation.py

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):

        radius = 5

        print("Area :", 3.14 * radius * radius)


obj = Circle()

obj.area()