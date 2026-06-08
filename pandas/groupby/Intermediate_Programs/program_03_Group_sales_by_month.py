#program_03_Group_sales_by_month.py

import pandas as pd

df = pd.DataFrame({
    "Month":["Jan","Jan","Feb","Feb"],
    "Sales":[1000,2000,1500,2500]
})

print(
    df.groupby("Month")["Sales"].sum()
)