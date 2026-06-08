# program_01_Secure_banking_system.py

class Bank:

    def __init__(self):

        # Private variable
        # Cannot access directly outside class
        self.__balance = 10000

    def deposit(self, amount):

        # Updating private balance safely
        self.__balance += amount

    def show_balance(self):

        print("Balance :", self.__balance)


obj = Bank()

obj.deposit(5000)

obj.show_balance()