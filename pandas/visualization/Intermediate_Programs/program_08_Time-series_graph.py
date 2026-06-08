#program_08_Time-series_graph.py

import pandas as pd

df = pd.DataFrame({
    "Date":pd.date_range(
        "2025-01-01",
        periods=5
    ),
    "Sales":[100,200,150,250,300]
})

df.plot(
    x="Date",
    y="Sales"
)

plt.show()