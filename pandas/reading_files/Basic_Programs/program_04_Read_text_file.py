#program_04_Read_text_file.py

import pandas as pd

df = pd.read_csv(
    "employees.txt",
    delimiter=","
)

print(df)