#program_05_Count_unique_values.py

import pandas as pd

s = pd.Series([10,20,20,30,30,40])

print("Unique Count =", s.nunique())