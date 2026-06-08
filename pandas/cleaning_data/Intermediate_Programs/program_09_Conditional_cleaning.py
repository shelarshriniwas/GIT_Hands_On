#program_09_Conditional_cleaning.py

import pandas as pd

df = pd.DataFrame({
    "Salary":[
        -5000,
        30000,
        40000
    ]
})

df.loc[
    df["Salary"] < 0,
    "Salary"
] = 0

print(df)