import pickle

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Rahul", 90)

with open("student.pkl", "wb") as f:
    pickle.dump(s, f)

print("Student stored")