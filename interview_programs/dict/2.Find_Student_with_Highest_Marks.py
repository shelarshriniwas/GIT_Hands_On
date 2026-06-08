'''
Program 2.Find_Student_with_Highest_Marks
students = {
    "A": 80,
    "B": 95,
    "C": 75
}

Output:

B 95

'''

students = {
    "A": 80,
    "B": 95,
    "C": 75
}

# Find student with highest marks
student = max(students, key=students.get)

print(student, students[student])


# Another Logic

students2 = {
    "A": 89,
    "B": 75,
    "C": 45
}

highest_student = ""
highest_marks = 0

for name, marks in students2.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

print(highest_student, highest_marks)