#program_06_Data_Validation_System.py

import pandas as pd

df = pd.DataFrame({
    "Age":[20,-5,30]
})

invalid = df[
    df["Age"] < 0
]

print(invalid)