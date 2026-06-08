# program_02_Cab_booking_system.py

from abc import ABC, abstractmethod

class Cab(ABC):

    @abstractmethod
    def book(self):
        pass


class MiniCab(Cab):

    def book(self):

        print("Mini Cab Booked")


obj = MiniCab()

obj.book()