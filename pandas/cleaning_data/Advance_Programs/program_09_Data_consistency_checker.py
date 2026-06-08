#program_09_Data_consistency_checker.py

import pandas as pd

df = pd.DataFrame({
    "Age":[
        20,
        30,
        "Thirty"
    ]
})

print(
    pd.to_numeric(
        df["Age"],
        errors="coerce"
    )
)