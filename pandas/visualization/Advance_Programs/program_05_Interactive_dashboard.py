#program_05_Interactive_dashboard.py

import pandas as pd

df = pd.DataFrame({
    "Sales":[100,200,300]
})

df.plot()

plt.show()