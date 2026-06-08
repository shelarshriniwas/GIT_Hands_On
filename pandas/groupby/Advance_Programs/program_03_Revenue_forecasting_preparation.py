#program_03_Revenue_forecasting_preparation.py

import pandas as pd

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Revenue":[1000,1500,2000]
})

monthly = sales.groupby(
    "Month"
)["Revenue"].sum()

print(monthly)