#program_01_Line_chart.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr"],
    "Sales":[1000,2000,1500,3000]
})

plt.plot(df["Month"], df["Sales"])
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()