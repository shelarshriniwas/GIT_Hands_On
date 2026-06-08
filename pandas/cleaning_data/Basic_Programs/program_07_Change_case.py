#program_07_Change_case.py

import pandas as pd

df = pd.DataFrame({
    "Name":["john","sam"]
})

df["Name"] = df["Name"].str.title()

print(df)