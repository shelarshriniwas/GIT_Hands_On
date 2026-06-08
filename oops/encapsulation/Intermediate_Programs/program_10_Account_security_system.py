# program_10_Account_security_system.py

class Security:

    def __init__(self):

        self.__password = "python123"

    def login(self, password):

        if password == self.__password:

            print("Access Granted")

        else:

            print("Access Denied")


obj = Security()

obj.login("python123")