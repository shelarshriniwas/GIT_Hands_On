#program_02_Sort_records.py
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[40,20,30]
})

print(df.sort_values("Age"))