#program_08_AI-ready_dataset_preparation.py

import pandas as pd

df = pd.read_csv(
    "dataset.csv"
)

df.fillna(
    df.mean(
        numeric_only=True
    ),
    inplace=True
)

df.drop_duplicates(
    inplace=True
)

print(df.head())