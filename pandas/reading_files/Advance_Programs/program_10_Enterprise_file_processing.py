#program_10_Enterprise_file_processing.py

import pandas as pd
import glob

files = glob.glob(
    "enterprise_data/*.csv"
)

master_df = pd.DataFrame()

for file in files:
    df = pd.read_csv(file)

    master_df = pd.concat(
        [master_df, df]
    )

master_df.drop_duplicates(
    inplace=True
)

master_df.to_csv(
    "enterprise_master.csv",
    index=False
)

print(
    "Records:",
    len(master_df)
)