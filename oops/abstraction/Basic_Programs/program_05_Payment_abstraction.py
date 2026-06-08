# program_05_Payment_abstraction.py

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def payment_method(self):
        pass


class CreditCard(Payment):

    def payment_method(self):

        print("Payment Through Credit Card")


obj = CreditCard()

obj.payment_method()