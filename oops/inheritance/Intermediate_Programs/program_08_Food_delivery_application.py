# program_08_Food_delivery_application.py

class Delivery:

    def address(self):

        print("Delivery Address Verified")


class Swiggy(Delivery):

    def tracking(self):

        print("Order Tracking Started")


obj = Swiggy()

obj.address()
obj.tracking()