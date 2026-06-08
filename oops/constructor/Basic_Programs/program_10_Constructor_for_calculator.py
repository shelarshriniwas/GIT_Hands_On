# program_10_Constructor_for_calculator.py

class calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("This is Calculator: ")
        c = self.a + self.b
        print("Addition: ",c)    

obj = calculator(5000, 12354)

print(obj.a)
print(obj.b)
obj.display()