#program_02_Bar_chart.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Product":["A","B","C"],
    "Sales":[100,200,150]
})

plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales")
plt.show()