#program_08_Data_migration_tool.py

import pandas as pd

old_data = pd.read_csv(
    "old_system.csv"
)

old_data.to_excel(
    "new_system.xlsx",
    index=False
)