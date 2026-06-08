#program_04_Remove_invalid_records.py

import pandas as pd

df = pd.DataFrame({
    "Age":[25,-10,30]
})

df = df[
    df["Age"] >= 0
]

print(df)