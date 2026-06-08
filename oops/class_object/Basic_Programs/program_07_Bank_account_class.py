# program_07_Bank_account_class.py

class Bank:

    balance = 1000

    def deposit(self, amount):
        self.balance += amount

obj = Bank()

obj.deposit(500)

print(obj.balance)