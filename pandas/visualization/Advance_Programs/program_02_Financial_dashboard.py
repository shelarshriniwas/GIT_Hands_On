#program_02_Financial_dashboard.py

import pandas as pd

finance = pd.DataFrame({
    "Month":["Jan","Feb","Mar"],
    "Profit":[1000,2000,3000]
})

finance.plot(
    x="Month",
    y="Profit"
)

plt.show()