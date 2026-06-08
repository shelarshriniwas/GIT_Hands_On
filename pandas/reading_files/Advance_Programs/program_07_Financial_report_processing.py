#program_07_Financial_report_processing.py

import pandas as pd

df = pd.read_excel(
    "finance.xlsx"
)

print(
    "Total Revenue:",
    df["Revenue"].sum()
)

print(
    "Total Profit:",
    df["Profit"].sum()
)