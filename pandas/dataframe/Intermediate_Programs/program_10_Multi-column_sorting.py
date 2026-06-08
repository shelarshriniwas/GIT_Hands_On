#program_10_Multi-column_sorting.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[30,30,20],
    "Salary":[50000,40000,30000]
})

print(
    df.sort_values(
        by=["Age","Salary"]
    )
)