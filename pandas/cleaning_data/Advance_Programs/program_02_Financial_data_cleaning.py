#program_02_Financial_data_cleaning.py

import pandas as pd

finance = pd.DataFrame({
    "Amount":[
        1000,
        None,
        5000
    ]
})

finance["Amount"] = (
    finance["Amount"]
    .fillna(
        finance["Amount"]
        .median()
    )
)

print(finance)