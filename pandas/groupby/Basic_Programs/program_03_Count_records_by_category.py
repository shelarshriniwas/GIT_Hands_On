#program_03_Count_records_by_category.py

import pandas as pd

df = pd.DataFrame({
    "Category":["A","B","A","C","B"]
})

print(df.groupby("Category").size())