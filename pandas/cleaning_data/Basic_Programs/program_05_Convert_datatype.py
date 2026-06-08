#program_05_Convert_datatype.py

import pandas as pd

df = pd.DataFrame({
    "Age":["20","30","40"]
})

df["Age"] = df["Age"].astype(int)

print(df.dtypes)