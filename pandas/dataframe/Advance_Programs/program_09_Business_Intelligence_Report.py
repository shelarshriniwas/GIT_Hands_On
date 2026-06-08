#program_09_Business_Intelligence_Report.py

import pandas as pd

sales = pd.DataFrame({
    "Region":["East","West","East","West"],
    "Sales":[1000,2000,3000,4000]
})

report = sales.groupby(
    "Region"
)["Sales"].sum()

print(report)