#program_02_Read_multiple_sheets.py

import pandas as pd

sheets = pd.read_excel(
    "employees.xlsx",
    sheet_name=None
)

for name, data in sheets.items():
    print(name)
    print(data)