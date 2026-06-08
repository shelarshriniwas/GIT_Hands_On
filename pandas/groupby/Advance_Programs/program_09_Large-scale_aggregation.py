#program_09_Large-scale_aggregation.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Category":
    np.random.choice(
        ["A","B","C"],
        100000
    ),
    "Value":
    np.random.randint(
        1,
        100,
        100000
    )
})

print(
    df.groupby("Category")
      ["Value"]
      .sum()
)