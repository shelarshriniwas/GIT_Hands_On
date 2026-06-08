#program_08_Print_last_values.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

print(s.tail())
print(s.tail(2))