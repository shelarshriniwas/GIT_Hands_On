#program_09_Count_columns.py

import pandas as pd

df = pd.read_csv("employees.csv")

print("Columns =", len(df.columns))