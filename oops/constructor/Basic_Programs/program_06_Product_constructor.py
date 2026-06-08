# program_06_Product_constructor.py

class Product:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

obj = Product("Parle-G", 10)

print(obj.name)
print(obj.amount)