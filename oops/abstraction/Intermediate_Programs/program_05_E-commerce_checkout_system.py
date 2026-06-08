# program_05_E-commerce_checkout_system.py
from abc import ABC, abstractmethod

class Order(ABC):

    @abstractmethod
    def confirm(self):
        pass


class Amazon(Order):

    def confirm(self):

        print("Amazon Order Confirmed")


obj = Amazon()

obj.confirm()