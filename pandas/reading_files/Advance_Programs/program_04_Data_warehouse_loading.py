#program_04_Data_warehouse_loading.py

import pandas as pd

df = pd.read_csv("transactions.csv")

df.to_sql(
    "transactions",
    con=connection,
    if_exists="append"
)