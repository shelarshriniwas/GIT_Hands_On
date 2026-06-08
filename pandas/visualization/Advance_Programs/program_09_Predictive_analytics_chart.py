#program_09_Predictive_analytics_chart.py

import pandas as pd

df = pd.DataFrame({
    "Month":[1,2,3,4,5],
    "Sales":[100,150,200,250,300]
})

df.plot(
    x="Month",
    y="Sales"
)

plt.show()