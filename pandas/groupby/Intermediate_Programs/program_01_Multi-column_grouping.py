#program_01_Multi-column_grouping.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","IT","HR","HR"],
    "City":["Pune","Mumbai","Pune","Mumbai"],
    "Salary":[50000,60000,40000,45000]
})

print(
    df.groupby(
        ["Department","City"]
    )["Salary"].sum()
)