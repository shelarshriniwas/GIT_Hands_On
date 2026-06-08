#program_08_Business_KPI_dashboard.py

import pandas as pd

sales = pd.DataFrame({
    "Region":["East","West"],
    "Sales":[10000,15000],
    "Profit":[2000,4000]
})

kpi = sales.groupby(
    "Region"
).agg({
    "Sales":"sum",
    "Profit":"sum"
})

print(kpi)