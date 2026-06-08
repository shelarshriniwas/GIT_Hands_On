#program_05_Missing_value_statistics.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A":[1,np.nan,3],
    "B":[np.nan,2,3]
})

print(df.isnull().sum())