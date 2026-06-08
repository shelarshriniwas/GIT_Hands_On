# program_05_Online_payment_gateway.py

class CreditCard:

    def payment(self):

        print("Credit Card Payment")


class DebitCard:

    def payment(self):

        print("Debit Card Payment")


c = CreditCard()
d = DebitCard()

c.payment()
d.payment()