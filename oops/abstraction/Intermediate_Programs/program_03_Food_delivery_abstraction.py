# program_03_Food_delivery_abstraction.py
from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def menu(self):
        pass


class PizzaShop(Restaurant):

    def menu(self):

        print("Pizza Available")


obj = PizzaShop()

obj.menu()