#program_09_Drop_rows.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"]
})

df = df.drop(1)

print(df)