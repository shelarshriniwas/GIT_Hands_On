# program_08_Food_ordering_app.py

class FoodOrder:

    def __init__(self, food_name, quantity, price):
        self.food_name = food_name
        self.quantity = quantity
        self.price = price

    def bill(self):

        total = self.quantity * self.price

        print("\n------ FOOD BILL ------")
        print("Food Item :", self.food_name)
        print("Quantity :", self.quantity)
        print("Price :", self.price)
        print("Total Bill :", total)


food = input("Enter Food Name : ")
quantity = int(input("Enter Quantity : "))
price = int(input("Enter Price : "))

obj = FoodOrder(food, quantity, price)

obj.bill()