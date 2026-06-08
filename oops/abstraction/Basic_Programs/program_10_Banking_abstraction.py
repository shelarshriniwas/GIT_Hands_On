# program_10_Banking_abstraction.py

from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest_rate(self):
        pass


class SBI(Bank):

    def interest_rate(self):

        print("Interest Rate : 7%")


obj = SBI()

obj.interest_rate()