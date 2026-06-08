#program_10_Groupby_optimization.py

import pandas as pd

df = pd.read_csv("sales.csv")

df["Region"] = (
    df["Region"]
    .astype("category")
)

result = (
    df.groupby("Region")
      ["Sales"]
      .sum()
)

print(result)