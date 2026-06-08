#program_01_Remove_null_values.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":["John","Sam",None],
    "Age":[25,np.nan,30]
})

df = df.dropna()

print(df)