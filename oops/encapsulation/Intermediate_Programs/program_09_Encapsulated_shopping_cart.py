# program_09_Encapsulated_shopping_cart.py

class Cart:

    def __init__(self):

        self.__items = []

    def add_item(self, item):

        self.__items.append(item)

    def show_items(self):

        print("Cart Items :", self.__items)


obj = Cart()

obj.add_item("Laptop")
obj.add_item("Mouse")

obj.show_items()