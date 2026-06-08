#program_02_Multiple_bar_chart.py

import pandas as pd

df = pd.DataFrame({
    "Sales":[100,200,300],
    "Profit":[20,40,60]
})

df.plot(kind="bar")

plt.show()