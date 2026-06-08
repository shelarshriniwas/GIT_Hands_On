# program_01_Create_dictionary.py

# Empty Dictionary
student = {}

# Take User Input
student_id = input("Enter Student ID : ")
name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
course = input("Enter Course : ")
marks = float(input("Enter Marks : "))

# Store Data In Dictionary
student[student_id] = {
    "name": name,
    "age": age,
    "course": course,
    "marks": marks
}

# Print Dictionary
print("\nStudent Dictionary")
print(student)