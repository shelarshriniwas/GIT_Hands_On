# program_02_User_authentication_system.py

class User:

    def __init__(self):

        self.__otp = 5678

    def verify(self, otp):

        if otp == self.__otp:

            print("OTP Verified")

        else:

            print("Invalid OTP")


obj = User()

obj.verify(5678)