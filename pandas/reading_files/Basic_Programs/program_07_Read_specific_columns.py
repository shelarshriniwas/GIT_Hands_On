#program_07_Read_specific_columns.py

import pandas as pd

df = pd.read_csv(
    "employees.csv",
    usecols=["Name", "Salary"]
)

print(df)