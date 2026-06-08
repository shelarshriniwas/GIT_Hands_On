#program_09_Index_manipulation.py

import pandas as pd

s = pd.Series([10,20,30])

s.index = ["A","B","C"]

print(s)