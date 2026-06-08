#program_04_Print_columns.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Age":[20,25]
})

print(df.columns)