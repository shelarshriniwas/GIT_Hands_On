# program_01_Banking_system_inheritance.py
class Bank:

    def bank_name(self):

        print("SBI Bank")


class Customer(Bank):

    def account_details(self):

        print("Savings Account")


obj = Customer()

obj.bank_name()
obj.account_details()