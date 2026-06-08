#program_09_Display_groups.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","HR","IT"],
    "Salary":[50000,40000,60000]
})

groups = df.groupby("Department")

for name, data in groups:
    print("Group:", name)
    print(data)