#program_08_Update_records.py
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Salary":[30000,40000]
})

df.loc[0,"Salary"] = 50000

print(df)