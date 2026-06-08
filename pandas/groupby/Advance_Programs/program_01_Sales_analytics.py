#program_01_Sales_analytics.py

import pandas as pd

sales = pd.DataFrame({
    "Region":["East","West","East"],
    "Sales":[10000,20000,15000]
})

report = sales.groupby(
    "Region"
)["Sales"].agg(
    ["sum","mean","max"]
)

print(report)