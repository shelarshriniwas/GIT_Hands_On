# program_08_ATM_abstraction.py

from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SBIATM(ATM):

    def withdraw(self):

        print("Cash Withdrawn")


obj = SBIATM()

obj.withdraw()