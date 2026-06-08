# program_08_Constructor_calling_methods.py

class Bank:

    def __init__(self, name, acc_id):
        self.name = name
        self.acc_id = acc_id

    def display(self):
        print("This is Display ()")

obj = Bank("Rahul", 12354)

print(obj.name)
print(obj.acc_id)
obj.display()