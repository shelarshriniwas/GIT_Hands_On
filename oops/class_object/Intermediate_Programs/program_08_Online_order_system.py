# program_08_Online_order_system.py

class Online_order:

    def items(self, amount):

        if amount >= 500 and amount <= 1000:
            print("order available")

        else:
            print("order not available")

obj = Online_order()

obj.items(950)