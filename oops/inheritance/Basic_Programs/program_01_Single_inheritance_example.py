# program_01_Single_inheritance_example.py
# Parent Class
class Father:

    def bike(self):

        print("Father Has Bike")


# Child Class inheriting Father
class Son(Father):

    def laptop(self):

        print("Son Has Laptop")


obj = Son()

# Accessing parent method
obj.bike()

# Accessing child method
obj.laptop()