#program_10_User-defined_grouping.py

import pandas as pd

df = pd.DataFrame({
    "Marks":[45,65,85,90]
})

df["Grade"] = df["Marks"].apply(
    lambda x:
    "Pass" if x >= 50
    else "Fail"
)

print(
    df.groupby("Grade")
      .size()
)