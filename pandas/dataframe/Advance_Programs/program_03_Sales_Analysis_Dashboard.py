#program_03_Sales_Analysis_Dashboard.py

import pandas as pd

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Sales":[10000,12000,15000]
})

print("Total Sales")
print(sales["Sales"].sum())

print("Average Sales")
print(sales["Sales"].mean())