#program_02_Normalize_data.py

import pandas as pd

df = pd.DataFrame({
    "Marks":[20,40,60,80,100]
})

df["Normalized"] = (
    (df["Marks"] - df["Marks"].min())
    /
    (df["Marks"].max() - df["Marks"].min())
)

print(df)