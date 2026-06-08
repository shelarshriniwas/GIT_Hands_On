#program_01_Multiple_line_chart.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Sales":[100,200,300],
    "Profit":[20,40,60]
})

plt.plot(df["Month"], df["Sales"])
plt.plot(df["Month"], df["Profit"])

plt.legend(["Sales","Profit"])
plt.show()