# program_10_Restaurant_billing_system.py

class Restaurant:

    def bill(self):
        basic = 500
        food_bill = int(input("enter food bill: "))

        print(basic + food_bill)

obj = Restaurant()

obj.bill()
