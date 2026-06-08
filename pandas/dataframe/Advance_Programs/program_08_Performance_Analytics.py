#program_08_Performance_Analytics.py

import pandas as pd

employees = pd.DataFrame({
    "Name":["A","B","C"],
    "Score":[80,90,70]
})

print(
    employees.sort_values(
        "Score",
        ascending=False
    )
)