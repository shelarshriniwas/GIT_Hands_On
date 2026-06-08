#program_01_ETL_pipeline.py

import pandas as pd

# Extract
df = pd.read_csv("sales.csv")

# Transform
df["Sales"] = df["Sales"] * 1.10

# Load
df.to_csv(
    "processed_sales.csv",
    index=False
)

print("ETL Completed")