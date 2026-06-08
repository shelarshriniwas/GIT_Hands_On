# program_03_Attendance_system_using_tuples.py

attendance = (
    ("Rahul", "Present"),
    ("Amit", "Absent"),
    ("Sneha", "Present")
)

for student, status in attendance:
    print(student, status)