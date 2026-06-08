#program_03_Find_duplicates.py
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","A"]
})

print(df.duplicated())