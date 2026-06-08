#program_05_Customer_Segmentation.py

import pandas as pd

customers = pd.DataFrame({
    "Customer":["A","B","C"],
    "Purchase":[5000,20000,10000]
})

customers["Category"] = customers[
    "Purchase"
].apply(
    lambda x:
    "Premium"
    if x > 15000
    else "Regular"
)

print(customers)