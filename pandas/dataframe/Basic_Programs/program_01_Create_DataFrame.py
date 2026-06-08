#program_01_Create_DataFrame.py

import pandas as pd

data = {
    "Name": ["John", "Sam", "David"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)

print(df)