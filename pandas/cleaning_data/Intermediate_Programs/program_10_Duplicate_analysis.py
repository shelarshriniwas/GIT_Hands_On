#program_10_Duplicate_analysis.py

import pandas as pd

df = pd.DataFrame({
    "Name":[
        "John",
        "Sam",
        "John"
    ]
})

print(
    df[df.duplicated()]
)