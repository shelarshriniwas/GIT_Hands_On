#program_10_Drop_columns.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A"],
    "Age":[20],
    "Salary":[50000]
})

df = df.drop(
    "Salary",
    axis=1
)

print(df)