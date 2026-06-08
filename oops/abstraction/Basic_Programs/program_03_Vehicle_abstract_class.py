# program_03_Vehicle_abstract_class.py

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass


class Bike(Vehicle):

    def fuel_type(self):

        print("Bike Uses Petrol")


obj = Bike()

obj.fuel_type()