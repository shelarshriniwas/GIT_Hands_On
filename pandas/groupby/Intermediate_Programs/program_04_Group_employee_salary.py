#program_04_Group_employee_salary.py

import pandas as pd

df = pd.DataFrame({
    "Department":["IT","HR","IT"],
    "Salary":[50000,40000,60000]
})

print(
    df.groupby("Department")["Salary"]
      .agg(["sum","mean"])
)