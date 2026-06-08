#program_01_Group_by_department.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","HR","IT","HR"],
    "Salary":[50000,40000,60000,45000]
})

result = df.groupby("Department")["Salary"].sum()

print(result)