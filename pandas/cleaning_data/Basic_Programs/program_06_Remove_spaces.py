#program_06_Remove_spaces.py

import pandas as pd

df = pd.DataFrame({
    "Name":[" John "," Sam "]
})

df["Name"] = df["Name"].str.strip()

print(df)