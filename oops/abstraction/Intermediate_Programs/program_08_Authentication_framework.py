# program_08_Authentication_framework.py
from abc import ABC, abstractmethod

class Verification(ABC):

    @abstractmethod
    def verify(self):
        pass


class OTPVerification(Verification):

    def verify(self):

        print("OTP Verified Successfully")


obj = OTPVerification()

obj.verify()