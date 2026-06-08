#program_10_Check_missing_values.py

import pandas as pd

df = pd.read_csv("employees.csv")

print(df.isnull().sum())