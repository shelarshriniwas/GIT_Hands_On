#program_04_Financial_Data_Analysis.py

import pandas as pd

finance = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Profit":[1000,1500,2000]
})

print(finance.describe())