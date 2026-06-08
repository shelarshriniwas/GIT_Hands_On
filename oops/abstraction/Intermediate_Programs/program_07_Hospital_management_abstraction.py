# program_07_Hospital_management_abstraction.py
from abc import ABC, abstractmethod

class Doctor(ABC):

    @abstractmethod
    def duty(self):
        pass


class Surgeon(Doctor):

    def duty(self):

        print("Performs Surgery")


obj = Surgeon()

obj.duty()