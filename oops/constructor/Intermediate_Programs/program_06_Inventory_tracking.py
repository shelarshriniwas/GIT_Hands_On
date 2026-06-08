# program_06_Inventory_tracking.py

class Inventory:

    def __init__(self, item_name, stock):
        self.item_name = item_name
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def display(self):
        print("Item :", self.item_name)
        print("Available Stock :", self.stock)


obj = Inventory("Keyboard", 20)

obj.display()

obj.update_stock(10)

print("\nAfter Stock Update")

obj.display()