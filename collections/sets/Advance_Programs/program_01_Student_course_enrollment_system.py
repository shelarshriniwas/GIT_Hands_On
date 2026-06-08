# program_01_Student_course_enrollment_system.py

student_courses = set()

student_courses.add("Python")
student_courses.add("AWS")
student_courses.add("Docker")

print("Enrolled Courses :", student_courses)

student_courses.remove("AWS")

print("Updated Courses :", student_courses)

student2 = {"AWS", "Linux", "Python"}

common_courses = student_courses & student2

print("Common Courses :", common_courses)