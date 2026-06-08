#program_02_Fill_null_values.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Age":[20,np.nan,30]
})

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

print(df)