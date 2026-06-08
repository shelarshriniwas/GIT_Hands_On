#program_04_Rename_columns.py

import pandas as pd

df = pd.DataFrame({
    "emp_name":["John"],
    "emp_salary":[50000]
})

df.rename(
    columns={
        "emp_name":"Name",
        "emp_salary":"Salary"
    },
    inplace=True
)

print(df)