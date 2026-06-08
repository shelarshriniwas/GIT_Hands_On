#program_06_Display_last_rows.py

import pandas as pd

df = pd.read_csv("employees.csv")

print(df.tail())