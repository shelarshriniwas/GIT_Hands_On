#program_07_Skip_rows.py

import pandas as pd

df = pd.read_csv(
    "employees.csv",
    skiprows=2
)

print(df)