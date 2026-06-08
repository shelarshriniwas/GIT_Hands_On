#program_09_Group_by_ranges.py

import pandas as pd

df = pd.DataFrame({
    "Age":[18,22,35,45,60]
})

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,20,40,60],
    labels=[
        "Young",
        "Adult",
        "Senior"
    ]
)

print(
    df.groupby("Age_Group")
      .size()
)