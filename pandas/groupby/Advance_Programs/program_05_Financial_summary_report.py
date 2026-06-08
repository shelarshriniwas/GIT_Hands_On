#program_05_Financial_summary_report.py

import pandas as pd

finance = pd.DataFrame({
    "Type":["Income","Expense",
            "Income","Expense"],
    "Amount":[10000,4000,
              15000,5000]
})

print(
    finance.groupby("Type")
           ["Amount"]
           .sum()
)