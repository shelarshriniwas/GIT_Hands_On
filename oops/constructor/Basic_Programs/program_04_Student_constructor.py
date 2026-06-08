# program_04_Student_constructor.py

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

obj = Student("Rahul", 90)

print(obj.name)
print(obj.marks)