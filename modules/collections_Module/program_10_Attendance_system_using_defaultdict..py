#Attendance system using defaultdict.

from collections import defaultdict

attendance = defaultdict(list)

date = input("Enter Date : ")

attendance[date].append("Shri")
attendance[date].append("Ram")

print(attendance)