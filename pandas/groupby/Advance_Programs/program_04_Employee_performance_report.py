#program_04_Employee_performance_report.py

import pandas as pd

employees = pd.DataFrame({
    "Department":["IT","IT","HR"],
    "Score":[80,90,75]
})

report = employees.groupby(
    "Department"
)["Score"].mean()

print(report)