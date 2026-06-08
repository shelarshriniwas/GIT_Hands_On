# program_03_Car_showroom_system.py

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)


car1 = Car("BMW", "X5", 9500000)

car1.display()