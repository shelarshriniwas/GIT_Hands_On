#program_10_Merge_imported_files.py

import pandas as pd

df1 = pd.read_csv("employee.csv")
df2 = pd.read_csv("salary.csv")

result = pd.merge(
    df1,
    df2,
    on="EmpID"
)

print(result)