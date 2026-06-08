# Create namedtuple for student.
from collections import namedtuple

Student = namedtuple("Student", ["id", "name", "marks"])

s1 = Student(101, "Shri", 90)

print("ID :", s1.id)
print("Name :", s1.name)
print("Marks :", s1.marks)