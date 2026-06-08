#program_03_Rolling_average.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

rolling_avg = s.rolling(2).mean()

print(rolling_avg)