#program_09_Read_compressed_files.py

import pandas as pd

df = pd.read_csv(
    "employees.zip",
    compression="zip"
)

print(df)