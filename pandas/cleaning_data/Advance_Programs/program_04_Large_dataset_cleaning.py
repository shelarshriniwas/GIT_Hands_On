#program_04_Large_dataset_cleaning.py

import pandas as pd

df = pd.read_csv(
    "large_file.csv"
)

df.drop_duplicates(
    inplace=True
)

df.fillna(
    0,
    inplace=True
)

print(df.head())