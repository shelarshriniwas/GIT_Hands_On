#program_08_Count_rows.py

import pandas as pd

df = pd.read_csv("employees.csv")

print("Rows =", len(df))