# program_33_attendance_management_system.py

with open("attendance.txt", "a") as file:

    student = input("Enter Student Name : ")

    file.write(student + " Present\n")

print("Attendance Marked")