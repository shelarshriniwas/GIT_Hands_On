#program_04_Change_Series_values.py

import pandas as pd

s = pd.Series([10, 20, 30])

s[1] = 100

print(s)