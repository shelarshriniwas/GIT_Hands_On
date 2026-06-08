#program_05_Add_column.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"]
})

df["Salary"] = [30000,40000]

print(df)