#program_08_Handle_missing_values.py

import pandas as pd

df = pd.read_csv(
    "employees.csv"
)

df.fillna(0, inplace=True)

print(df)