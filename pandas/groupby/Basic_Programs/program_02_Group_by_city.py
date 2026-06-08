#program_02_Group_by_city.py

import pandas as pd

df = pd.DataFrame({
    "City":["Pune","Mumbai","Pune","Delhi"],
    "Sales":[1000,2000,1500,3000]
})

print(df.groupby("City")["Sales"].sum())