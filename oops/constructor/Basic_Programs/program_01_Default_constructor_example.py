# program_01_Default_constructor_example.py
class Demo:

    def __init__(self):
        print("Constructor Called")

obj = Demo()


class Demo:

    def __init__(self):
        self.name = "Rahul"

obj = Demo()

print(obj.name)