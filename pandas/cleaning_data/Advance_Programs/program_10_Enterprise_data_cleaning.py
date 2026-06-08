#program_10_Enterprise_data_cleaning.py

import pandas as pd

df = pd.read_csv(
    "enterprise.csv"
)

df.drop_duplicates(
    inplace=True
)

df.fillna(
    "Unknown",
    inplace=True
)

df.columns = (
    df.columns
    .str.strip()
    .str.upper()
)

df.to_csv(
    "clean_enterprise.csv",
    index=False
)

print(
    "Cleaning Completed"
)