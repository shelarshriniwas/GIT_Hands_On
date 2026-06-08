#program_07_Rename_column.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Salary":[30000,40000]
})

df.rename(
    columns={"Salary":"Income"},
    inplace=True
)

print(df)