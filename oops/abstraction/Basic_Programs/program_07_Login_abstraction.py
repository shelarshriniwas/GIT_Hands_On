# program_07_Login_abstraction.py

from abc import ABC, abstractmethod

class Login(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class EmailLogin(Login):

    def authenticate(self):

        print("Login Using Email")


obj = EmailLogin()

obj.authenticate()