#program_07_Series_comparison.py

import pandas as pd

s1 = pd.Series([10,20,30])
s2 = pd.Series([10,25,30])

print(s1 == s2)