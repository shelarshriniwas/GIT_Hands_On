#program_04_Sum_values_by_category.py

import pandas as pd

df = pd.DataFrame({
    "Category":["A","B","A"],
    "Amount":[100,200,300]
})

print(df.groupby("Category")["Amount"].sum())