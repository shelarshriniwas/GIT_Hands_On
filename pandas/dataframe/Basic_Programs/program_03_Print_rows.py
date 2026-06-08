#program_03_Print_rows.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[20,25,30]
})

print(df.head())
print()
print(df.iloc[2])