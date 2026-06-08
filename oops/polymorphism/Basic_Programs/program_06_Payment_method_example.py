# program_06_Payment_method_example.py

class GooglePay:

    def payment(self):

        print("Payment Using GooglePay")


class PhonePe:

    def payment(self):

        print("Payment Using PhonePe")


g = GooglePay()
p = PhonePe()

g.payment()
p.payment()