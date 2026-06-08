#program_06_Data_quality_report.py

import pandas as pd

df = pd.read_csv(
    "employees.csv"
)

report = {
    "Rows": len(df),
    "Columns": len(df.columns),
    "Missing":
    df.isnull().sum().sum(),
    "Duplicates":
    df.duplicated().sum()
}

print(report)

