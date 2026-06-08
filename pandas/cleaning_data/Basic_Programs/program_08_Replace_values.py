#program_08_Replace_values.py

import pandas as pd

df = pd.DataFrame({
    "Gender":["M","F","M"]
})

df["Gender"] = df["Gender"].replace({
    "M":"Male",
    "F":"Female"
})

print(df)