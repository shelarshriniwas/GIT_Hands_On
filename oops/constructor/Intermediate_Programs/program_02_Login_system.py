# program_02_Login_system.py

class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login(self):

        if self.username == "admin" and self.password == "1234":
            print("Login Successful")

        else:
            print("Invalid Username or Password")


username = input("Enter Username : ")
password = input("Enter Password : ")

obj = Login(username, password)

obj.check_login()