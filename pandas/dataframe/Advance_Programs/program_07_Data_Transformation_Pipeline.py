#program_07_Data_Transformation_Pipeline.py

import pandas as pd

df = pd.DataFrame({
    "Name":["john","sam"],
    "Salary":[50000,60000]
})

df["Name"] = df["Name"].str.title()

df["Salary"] = (
    df["Salary"] * 1.10
)

print(df)