#program_01_Handle_outliers.py
import pandas as pd

df = pd.DataFrame({
    "Salary":[30000,35000,40000,500000]
})

q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

clean_df = df[
    (df["Salary"] >= lower)
    &
    (df["Salary"] <= upper)
]

print(clean_df)