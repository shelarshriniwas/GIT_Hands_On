#program_05_Import_large_files.py

import pandas as pd

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=1000
):
    print(chunk.head())