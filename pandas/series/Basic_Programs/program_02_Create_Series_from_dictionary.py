#program_02_Create_Series_from_dictionary.py

import pandas as pd

data = {
    "A": 100,
    "B": 200,
    "C": 300
}

s = pd.Series(data)

print(s)