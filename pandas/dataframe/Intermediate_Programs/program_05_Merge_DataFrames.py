#program_05_Merge_DataFrames.py
import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["A","B"]
})

df2 = pd.DataFrame({
    "ID":[1,2],
    "Salary":[30000,40000]
})

result = pd.merge(
    df1,
    df2,
    on="ID"
)

print(result)