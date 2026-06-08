#program_02_Student_Management_System.py

import pandas as pd

students = pd.DataFrame({
    "RollNo":[1,2,3],
    "Name":["Ram","Shyam","Mohan"],
    "Marks":[80,70,90]
})

print(students)

topper = students[
    students["Marks"] ==
    students["Marks"].max()
]

print(topper)