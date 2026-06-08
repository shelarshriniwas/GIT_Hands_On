#program_05_Group_customer_purchases.py

import pandas as pd

df = pd.DataFrame({
    "Customer":["A","B","A","C"],
    "Purchase":[500,1000,700,300]
})

print(
    df.groupby("Customer")
      ["Purchase"]
      .sum()
)