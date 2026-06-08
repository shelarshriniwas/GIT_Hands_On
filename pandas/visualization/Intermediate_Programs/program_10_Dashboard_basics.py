#program_10_Dashboard_basics.py

import pandas as pd

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Sales":[1000,2000,3000]
})

print(
    "Total Sales:",
    sales["Sales"].sum()
)

sales.plot(
    x="Month",
    y="Sales"
)

plt.show()