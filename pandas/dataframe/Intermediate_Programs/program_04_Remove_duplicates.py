#program_04_Remove_duplicates.py
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","A"]
})

print(df.drop_duplicates())