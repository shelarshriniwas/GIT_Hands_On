#program_03_Remove_duplicates.py

import pandas as pd

df = pd.DataFrame({
    "Name":["John","Sam","John"]
})

df = df.drop_duplicates()

print(df)