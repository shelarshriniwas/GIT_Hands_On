#program_07_Print_first_values.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

print(s.head())
print(s.head(3))