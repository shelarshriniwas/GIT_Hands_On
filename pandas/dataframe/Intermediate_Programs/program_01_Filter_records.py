#program_01_Filter_records.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[20,30,40]
})

print(df[df["Age"] > 25])