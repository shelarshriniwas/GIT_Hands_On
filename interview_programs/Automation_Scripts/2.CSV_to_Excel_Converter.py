'''
Input:

employees.csv

Output:

employees.xlsx Created
'''
# csv_to_excel.py

import pandas as pd

csv_file = "employees.csv"
excel_file = "employees.xlsx"

df = pd.read_csv(csv_file)

df.to_excel(
    excel_file,
    index=False
)

print("employees.xlsx Created")