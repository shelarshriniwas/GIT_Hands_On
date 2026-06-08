# program_09_Mobile_lock_system.py

class Mobile:

    def __init__(self):

        self.__password = "1234"

    def unlock(self, password):

        if password == self.__password:

            print("Mobile Unlocked")

        else:

            print("Wrong Password")


obj = Mobile()

pwd = input("Enter Password : ")

obj.unlock(pwd)