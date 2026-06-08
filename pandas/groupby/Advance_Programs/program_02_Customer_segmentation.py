#program_02_Customer_segmentation.py

import pandas as pd

customers = pd.DataFrame({
    "Customer":["A","B","C","D"],
    "Purchase":[500,2000,10000,300]
})

customers["Segment"] = pd.cut(
    customers["Purchase"],
    bins=[0,1000,5000,20000],
    labels=[
        "Low",
        "Medium",
        "High"
    ]
)

print(
    customers.groupby(
        "Segment"
    ).size()
)