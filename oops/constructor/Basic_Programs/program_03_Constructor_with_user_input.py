# program_03_Constructor_with_user_input.py

class User:

    def __init__(self):
        self.name = input("Enter Name : ")

obj = User()

print(obj.name)

class User:

    def __init__(self):
        self.name = input("Name : ")
        self.age = int(input("Age : "))

obj = User()

print(obj.name, obj.age)