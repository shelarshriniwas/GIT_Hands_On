#program_01_Time-series_creation.py

import pandas as pd

dates = pd.date_range(
    start="2025-01-01",
    periods=5
)

s = pd.Series(
    [100,110,120,130,140],
    index=dates
)

print(s)