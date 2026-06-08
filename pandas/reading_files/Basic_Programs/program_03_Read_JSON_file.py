#program_03_Read_JSON_file.py

import pandas as pd

df = pd.read_json("employees.json")

print(df)