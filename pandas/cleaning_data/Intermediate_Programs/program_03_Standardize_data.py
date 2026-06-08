#program_03_Standardize_data.py

import pandas as pd

df = pd.DataFrame({
    "Marks":[20,40,60,80,100]
})

df["Standardized"] = (
    (df["Marks"] -
    df["Marks"].mean())
    /
    df["Marks"].std()
)

print(df)