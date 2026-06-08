#program_10_Enterprise_reporting_dashboard.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","HR","Sales"],
    "Employees":[50,20,30]
})

df.plot(
    x="Department",
    y="Employees",
    kind="bar"
)

plt.show()