#program_05_Display_first_rows.py

import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head())