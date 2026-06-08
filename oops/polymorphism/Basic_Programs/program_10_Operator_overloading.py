# program_10_Operator_overloading.py

class Number:

    def __init__(self, value):

        self.value = value

    # Overloading + operator
    def __add__(self, other):

        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print("Addition :", n1 + n2)