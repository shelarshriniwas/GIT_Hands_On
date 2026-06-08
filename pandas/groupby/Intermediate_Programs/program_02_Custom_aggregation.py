#program_02_Custom_aggregation.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","IT","HR"],
    "Salary":[50000,60000,40000]
})

result = df.groupby(
    "Department"
)["Salary"].agg(
    lambda x: max(x)-min(x)
)

print(result)