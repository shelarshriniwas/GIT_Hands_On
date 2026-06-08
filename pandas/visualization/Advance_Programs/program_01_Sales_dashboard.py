#program_01_Sales_dashboard.py

import pandas as pd

sales = pd.DataFrame({
    "Region":["East","West"],
    "Sales":[10000,15000]
})

print(
    sales["Sales"].sum()
)

sales.plot(
    x="Region",
    y="Sales",
    kind="bar"
)

plt.show()