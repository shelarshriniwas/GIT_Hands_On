#program_05_Automated_cleaning_pipeline.py

import pandas as pd

def clean_data(df):

    df.drop_duplicates(
        inplace=True
    )

    df.fillna(
        0,
        inplace=True
    )

    return df

data = pd.read_csv(
    "data.csv"
)

cleaned = clean_data(data)

print(cleaned)