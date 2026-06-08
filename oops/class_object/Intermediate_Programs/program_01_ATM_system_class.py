# program_01_ATM_system_class.py

class ATM:

    balance = 5000

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)

obj = ATM()

obj.withdraw(1000)