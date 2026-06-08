#program_08_Data_validation.py

import pandas as pd

df = pd.DataFrame({
    "Email":[
        "abc@gmail.com",
        "wrong_email"
    ]
})

valid = df[
    df["Email"]
    .str.contains("@")
]

print(valid)