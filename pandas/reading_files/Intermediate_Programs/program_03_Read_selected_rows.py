#program_03_Read_selected_rows.py

import pandas as pd

df = pd.read_csv(
    "employees.csv",
    nrows=5
)

print(df)