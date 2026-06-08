#program_04_Monthly_revenue_graph.py

import pandas as pd

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Revenue":[5000,7000,6000]
})

df.plot(
    x="Month",
    y="Revenue",
    kind="line"
)

plt.show()