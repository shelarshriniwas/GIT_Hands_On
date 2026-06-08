# Use defaultdict for marks storage.
from collections import defaultdict

marks = defaultdict(list)

student = input("Enter Student Name : ")

for i in range(3):

    mark = int(input("Enter Mark : "))

    marks[student].append(mark)

print(marks)
