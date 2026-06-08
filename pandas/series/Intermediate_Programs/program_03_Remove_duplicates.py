#program_03_Remove_duplicates.py

import pandas as pd

s = pd.Series([10,20,20,30,30,40])

print(s.drop_duplicates())