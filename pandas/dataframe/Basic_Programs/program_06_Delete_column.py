#program_06_Delete_column.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Salary":[30000,40000]
})

df.drop("Salary", axis=1, inplace=True)

print(df)