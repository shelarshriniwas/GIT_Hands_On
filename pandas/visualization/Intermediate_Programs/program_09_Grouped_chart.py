#program_09_Grouped_chart.py

import pandas as pd

df = pd.DataFrame({
    "Sales":[100,200],
    "Profit":[30,50]
},
index=["East","West"])

df.plot(kind="bar")

plt.show()