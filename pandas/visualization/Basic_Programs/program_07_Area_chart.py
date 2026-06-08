#program_07_Area_chart.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Sales":[1000,2000,1500]
})

plt.fill_between(
    df["Month"],
    df["Sales"]
)

plt.show()