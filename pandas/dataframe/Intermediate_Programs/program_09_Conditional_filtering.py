#program_09_Conditional_filtering.py
import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[20,30,40],
    "Salary":[20000,50000,70000]
})

result = df[
    (df["Age"] > 25)
    &
    (df["Salary"] > 40000)
]

print(result)