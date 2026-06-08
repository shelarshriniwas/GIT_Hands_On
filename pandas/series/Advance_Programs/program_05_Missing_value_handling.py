#program_05_Missing_value_handling.py

import pandas as pd
import numpy as np

s = pd.Series([10,np.nan,30,np.nan])

s = s.fillna(s.mean())

print(s)