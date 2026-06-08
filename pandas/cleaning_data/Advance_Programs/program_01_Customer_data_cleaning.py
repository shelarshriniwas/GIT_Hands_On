#program_01_Customer_data_cleaning.py

import pandas as pd

customers = pd.DataFrame({
    "Name":[
        " john ",
        None,
        "SAM"
    ]
})

customers["Name"] = (
    customers["Name"]
    .fillna("Unknown")
    .str.strip()
    .str.title()
)

print(customers)