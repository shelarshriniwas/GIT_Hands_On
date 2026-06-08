#program_05_Incremental_file_loading.py

import pandas as pd

new_data = pd.read_csv(
    "daily_sales.csv"
)

master = pd.read_csv(
    "master_sales.csv"
)

updated = pd.concat(
    [master, new_data]
)

updated.to_csv(
    "master_sales.csv",
    index=False
)