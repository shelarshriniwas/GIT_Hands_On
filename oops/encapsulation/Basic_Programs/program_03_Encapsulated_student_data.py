# program_03_Encapsulated_student_data.py

class Student:

    def __init__(self):

        self.__name = ""
        self.__marks = 0

    def set_data(self, name, marks):

        self.__name = name
        self.__marks = marks

    def display(self):

        print("Name :", self.__name)
        print("Marks :", self.__marks)


obj = Student()

obj.set_data("Rahul", 85)

obj.display()

class Student:

    def __init__(self):

        self.__roll = 0

    def set_roll(self, roll):

        # Validation
        if roll > 0:
            self.__roll = roll

    def get_roll(self):

        return self.__roll


obj = Student()

obj.set_roll(101)

print("Roll Number :", obj.get_roll())