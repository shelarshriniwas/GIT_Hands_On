#program_07_Product_category_analysis.py

import pandas as pd

products = pd.DataFrame({
    "Category":[
        "Electronics",
        "Electronics",
        "Furniture"
    ],
    "Sales":[1000,2000,3000]
})

print(
    products.groupby(
        "Category"
    )["Sales"].sum()
)