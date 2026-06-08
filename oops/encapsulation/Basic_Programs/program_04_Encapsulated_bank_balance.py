# program_04_Encapsulated_bank_balance.py
class Bank:

    def __init__(self):

        self.__balance = 10000

    def deposit(self, amount):

        self.__balance += amount

    def show_balance(self):

        print("Balance :", self.__balance)


obj = Bank()

obj.deposit(5000)

obj.show_balance()

###################################################

class Bank:

    def __init__(self):

        self.__balance = 15000

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

        else:
            print("Insufficient Balance")

    def display(self):

        print("Remaining Balance :", self.__balance)


obj = Bank()

obj.withdraw(5000)

obj.display()