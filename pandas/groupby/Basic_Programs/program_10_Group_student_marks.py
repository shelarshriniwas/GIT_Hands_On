#program_10_Group_student_marks.py

import pandas as pd

df = pd.DataFrame({
    "Class":["A","A","B","B"],
    "Marks":[80,90,70,85]
})

print(df.groupby("Class")["Marks"].mean())