# program_08_OTP_verification_system.py

class OTP:

    def __init__(self):

        self.__otp = 123456

    def verify(self, otp):

        if otp == self.__otp:

            print("OTP Verified")

        else:

            print("Invalid OTP")


obj = OTP()

obj.verify(123456)