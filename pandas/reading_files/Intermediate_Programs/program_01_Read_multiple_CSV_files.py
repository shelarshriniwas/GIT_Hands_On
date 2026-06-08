#program_01_Read_multiple_CSV_files.py

import pandas as pd
import glob

files = glob.glob("data/*.csv")

for file in files:
    df = pd.read_csv(file)
    print(df.head())