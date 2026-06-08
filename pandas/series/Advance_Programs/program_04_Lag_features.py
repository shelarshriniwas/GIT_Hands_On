#program_04_Lag_features.py

import pandas as pd

s = pd.Series([100,200,300,400])

s_lag = s.shift(1)

print(s_lag)