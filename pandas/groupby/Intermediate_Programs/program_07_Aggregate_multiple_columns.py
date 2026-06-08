#program_07_Aggregate_multiple_columns.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","IT","HR"],
    "Salary":[50000,60000,40000],
    "Bonus":[5000,6000,4000]
})

print(
    df.groupby("Department")
      .agg({
          "Salary":"sum",
          "Bonus":"mean"
      })
)