#program_03_Sales_trend_chart.py

import pandas as pd

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr"],
    "Sales":[1000,1500,2000,2500]
})

sales.plot(
    x="Month",
    y="Sales"
)

plt.show()