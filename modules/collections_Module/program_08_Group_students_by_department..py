# Group students by department.
from collections import defaultdict

students = defaultdict(list)

students["IT"].append("Shri")
students["IT"].append("Ram")

students["CS"].append("Amit")

print(students)