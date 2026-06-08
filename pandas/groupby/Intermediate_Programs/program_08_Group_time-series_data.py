#program_08_Group_time-series_data.py

import pandas as pd

df = pd.DataFrame({
    "Date":pd.date_range(
        "2025-01-01",
        periods=6
    ),
    "Sales":[100,200,300,400,500,600]
})

df["Month"] = df["Date"].dt.month

print(
    df.groupby("Month")
      ["Sales"]
      .sum()
)