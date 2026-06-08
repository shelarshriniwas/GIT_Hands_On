# program_04_Secure_inventory_system.py

class Product:

    def __init__(self):

        self.__price = 0

    def set_price(self, price):

        if price > 0:

            self.__price = price

    def get_price(self):

        return self.__price


obj = Product()

obj.set_price(25000)

print("Price :", obj.get_price())