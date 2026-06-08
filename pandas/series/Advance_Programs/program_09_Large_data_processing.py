#program_09_Large_data_processing.py

import pandas as pd
import numpy as np

s = pd.Series(
    np.random.randint(
        1,
        100,
        1000000
    )
)

print("Mean =", s.mean())
print("Max =", s.max())