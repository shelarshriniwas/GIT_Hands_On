# program_07_Bank_account_constructor.py

class Bank:

    def __init__(self, name, acc_id):
        self.name = name
        self.acc_id = acc_id

obj = Bank("Rahul", 12354)

print(obj.name)
print(obj.acc_id)