#program_08_Business_intelligence_dashboard.py

import pandas as pd

df = pd.DataFrame({
    "Region":["East","West"],
    "Revenue":[10000,15000]
})

df.plot(
    x="Region",
    y="Revenue",
    kind="bar"
)

plt.show()