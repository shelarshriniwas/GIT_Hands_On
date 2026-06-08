#program_07_String_cleaning.py

import pandas as pd

df = pd.DataFrame({
    "Name":[
        " john ",
        " SAM "
    ]
})

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.title()
)

print(df)