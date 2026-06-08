#program_03_Customer_analytics_dashboard.py

import pandas as pd

customers = pd.DataFrame({
    "Age":[20,25,30,35,40]
})

customers.plot(
    kind="hist"
)

plt.show()