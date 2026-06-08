#program_09_Automated_reporting.py

import pandas as pd

df = pd.read_csv(
    "sales.csv"
)

report = df.groupby(
    "Region"
)["Sales"].sum()

report.to_csv(
    "sales_report.csv"
)

print(report)