#program_06_Date_formatting.py

import pandas as pd

df = pd.DataFrame({
    "Date":[
        "01/01/2025",
        "15/02/2025"
    ]
})

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True
)

print(df)