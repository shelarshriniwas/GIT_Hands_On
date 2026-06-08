# program_02_Getter_and_setter_methods.py
class Employee:

    def __init__(self):

        # Private variable
        self.__salary = 0

    # Setter method
    # Used to set value safely
    def set_salary(self, salary):

        self.__salary = salary

    # Getter method
    # Used to get private value
    def get_salary(self):

        return self.__salary


obj = Employee()

obj.set_salary(45000)

print("Salary :", obj.get_salary())


class Mobile:

    def __init__(self):

        self.__price = 0

    def set_price(self, price):

        # Validation added before assigning
        if price > 0:
            self.__price = price

    def get_price(self):

        return self.__price


obj = Mobile()

obj.set_price(25000)

print("Mobile Price :", obj.get_price())