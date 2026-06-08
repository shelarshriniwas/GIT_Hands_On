#program_10_Save_DataFrame.py

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B"],
    "Age":[20,25]
})

df.to_csv(
    "output.csv",
    index=False
)