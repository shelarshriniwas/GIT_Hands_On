#program_06_Join_DataFrames.py
import pandas as pd

df1 = pd.DataFrame(
    {"Name":["A","B"]},
    index=[1,2]
)

df2 = pd.DataFrame(
    {"Salary":[30000,40000]},
    index=[1,2]
)

print(df1.join(df2))