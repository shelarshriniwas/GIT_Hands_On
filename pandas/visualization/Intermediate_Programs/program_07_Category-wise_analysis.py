#program_07_Category-wise_analysis.py

import pandas as pd

df = pd.DataFrame({
    "Category":["A","B","A","B"],
    "Sales":[100,200,300,400]
})

df.groupby(
    "Category"
)["Sales"].sum().plot(
    kind="bar"
)

plt.show()