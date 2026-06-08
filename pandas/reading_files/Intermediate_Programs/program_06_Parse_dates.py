#program_06_Parse_dates.py

import pandas as pd

df = pd.read_csv(
    "employees.csv",
    parse_dates=["JoinDate"]
)

print(df.dtypes)