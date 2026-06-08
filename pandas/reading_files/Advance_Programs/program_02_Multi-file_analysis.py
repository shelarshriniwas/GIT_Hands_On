#program_02_Multi-file_analysis.py

import pandas as pd
import glob

files = glob.glob("sales/*.csv")

all_data = pd.concat(
    [pd.read_csv(file) for file in files]
)

print(all_data.describe())