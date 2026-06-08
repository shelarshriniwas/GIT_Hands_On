#program_04_Read_selected_columns.py

import pandas as pd

df = pd.read_csv(
    "employees.csv",
    usecols=["Name", "Age"]
)

print(df)