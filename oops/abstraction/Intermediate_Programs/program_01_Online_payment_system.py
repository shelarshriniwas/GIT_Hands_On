# program_01_Online_payment_system.py

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class GooglePay(Payment):

    def pay(self):

        print("Payment Using GooglePay")


obj = GooglePay()

obj.pay()