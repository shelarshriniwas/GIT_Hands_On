#program_10_Predictive_preprocessing.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

normalized = (
    (s - s.min()) /
    (s.max() - s.min())
)

print(normalized)