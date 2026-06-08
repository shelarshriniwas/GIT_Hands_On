# program_05_Invoice_generator.py

class Invoice:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def generate_bill(self):

        total = self.quantity * self.price

        print("\n------ INVOICE ------")
        print("Product :", self.product)
        print("Quantity :", self.quantity)
        print("Price :", self.price)
        print("Total :", total)


product = input("Enter Product Name : ")
quantity = int(input("Enter Quantity : "))
price = int(input("Enter Price : "))

obj = Invoice(product, quantity, price)

obj.generate_bill()