#program_06_KPI_visualization.py

import pandas as pd

sales = pd.DataFrame({
    "Sales":[1000,2000,3000]
})

print(
    "Average:",
    sales["Sales"].mean()
)

print(
    "Maximum:",
    sales["Sales"].max()
)