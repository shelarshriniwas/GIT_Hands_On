#program_05_Scatter_plot.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Hours":[1,2,3,4,5],
    "Marks":[40,50,60,80,90]
})

plt.scatter(
    df["Hours"],
    df["Marks"]
)

plt.show()