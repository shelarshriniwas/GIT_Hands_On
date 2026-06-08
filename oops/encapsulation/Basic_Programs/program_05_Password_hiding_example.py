# program_05_Password_hiding_example.py

class Login:

    def __init__(self):

        self.__password = "admin123"

    def login(self, password):

        if password == self.__password:

            print("Login Successful")

        else:

            print("Wrong Password")


obj = Login()

pwd = input("Enter Password : ")

obj.login(pwd)