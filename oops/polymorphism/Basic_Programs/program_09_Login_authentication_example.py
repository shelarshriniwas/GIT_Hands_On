# program_09_Login_authentication_example.py

class Admin:

    def login(self):

        print("Admin Login")


class User:

    def login(self):

        print("User Login")


a = Admin()
u = User()

a.login()
u.login()