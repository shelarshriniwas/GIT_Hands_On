#program_06_Market_basket_analysis.py

import pandas as pd

sales = pd.DataFrame({
    "Product":[
        "Laptop",
        "Mouse",
        "Laptop",
        "Keyboard"
    ]
})

print(
    sales.groupby("Product")
         .size()
)