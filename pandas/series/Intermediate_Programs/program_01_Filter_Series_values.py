#program_01_Filter_Series_values.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

result = s[s > 30]

print(result)