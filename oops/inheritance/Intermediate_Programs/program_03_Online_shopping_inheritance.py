# program_03_Online_shopping_inheritance.py

class Product:

    def details(self):

        print("Product Details")


class Mobile(Product):

    def features(self):

        print("Mobile Features")


obj = Mobile()

obj.details()
obj.features()