#program_09_Find_datatype.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Age":[20,25]
})

print(df.dtypes)