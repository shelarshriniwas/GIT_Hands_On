#program_09_Check_missing_values.py

import pandas as pd
import numpy as np

s = pd.Series([10, np.nan, 30])

print(s.isnull())