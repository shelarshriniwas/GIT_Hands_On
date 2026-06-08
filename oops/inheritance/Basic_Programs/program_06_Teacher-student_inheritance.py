# program_06_Teacher-student_inheritance.py

class Teacher:

    def subject(self):

        print("Teacher Teaches Python")


class Student(Teacher):

    def study(self):

        print("Student Studies Python")


obj = Student()

obj.subject()
obj.study()