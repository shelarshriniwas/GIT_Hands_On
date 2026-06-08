# program_09_E-commerce_product_system.py

class Product:

    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def display(self):
        print("Product Name :", self.product_name)
        print("Price :", self.price)
        print("Stock :", self.stock)


obj = Product("Laptop", 65000, 15)

obj.display()