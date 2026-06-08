#program_06_Top-performing_groups.py

import pandas as pd

df = pd.DataFrame({
    "Region":["East","West","East","North"],
    "Sales":[1000,5000,3000,2000]
})

result = (
    df.groupby("Region")
      ["Sales"]
      .sum()
      .sort_values(
          ascending=False
      )
)

print(result)