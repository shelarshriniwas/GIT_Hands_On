# program_10_ATM_pin_validation.py

class ATM:

    def __init__(self):

        self.__balance = 10000
        self.__pin = 1111

    def withdraw(self, pin, amount):

        if pin == self.__pin:

            if amount <= self.__balance:

                self.__balance -= amount

                print("Withdrawal Successful")

                print("Remaining Balance :", self.__balance)

            else:

                print("Insufficient Balance")

        else:

            print("Invalid PIN")


obj = ATM()

obj.withdraw(1111, 3000)