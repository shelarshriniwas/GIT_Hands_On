# program_05_Student_grade_system.py
class Student:

    def grade(self, marks):

        if marks >= 90:
            print("A")

        else:
            print("B")

obj = Student()

obj.grade(95)