# program_01_Abstract_class_example.py

from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Animal(ABC):

    # Abstract method
    # Child class must implement this method
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):

        print("Dog Barks")


obj = Dog()

obj.sound()