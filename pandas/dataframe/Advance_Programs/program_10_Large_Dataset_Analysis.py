#program_10_Large_Dataset_Analysis.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Numbers":
    np.random.randint(
        1,
        100,
        1000000
    )
})

print(
    "Mean =",
    df["Numbers"].mean()
)

print(
    "Max =",
    df["Numbers"].max()
)

print(
    "Min =",
    df["Numbers"].min()
)