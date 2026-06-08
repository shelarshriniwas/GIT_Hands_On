#program_03_Pie_chart.py

import pandas as pd
import matplotlib.pyplot as plt

sales = [30, 25, 20, 25]
labels = ["A", "B", "C", "D"]

plt.pie(
    sales,
    labels=labels,
    autopct="%1.1f%%"
)

plt.show()