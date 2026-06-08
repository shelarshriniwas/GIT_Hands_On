#program_07_Rule-based_cleaning.py

import pandas as pd

df = pd.DataFrame({
    "Age":[
        20,
        -5,
        150
    ]
})

df = df[
    (df["Age"] >= 0)
    &
    (df["Age"] <= 100)
]

print(df)