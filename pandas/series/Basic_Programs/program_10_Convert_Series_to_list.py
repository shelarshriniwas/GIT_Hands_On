#program_10_Convert_Series_to_list.py

import pandas as pd

s = pd.Series([10,20,30])

lst = s.tolist()

print(lst)