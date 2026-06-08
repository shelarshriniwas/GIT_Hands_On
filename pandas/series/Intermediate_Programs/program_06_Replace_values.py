#program_06_Replace_values.py

import pandas as pd

s = pd.Series([10,20,30])

s = s.replace(20, 200)

print(s)