# program_10_E-commerce_product_hierarchy.py

class Product:

    def category(self):

        print("Electronics Product")


class Mobile(Product):

    def mobile_name(self):

        print("iPhone 15")


obj = Mobile()

obj.category()
obj.mobile_name()