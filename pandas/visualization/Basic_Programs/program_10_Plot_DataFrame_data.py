#program_10_Plot_DataFrame_data.py

import pandas as pd

df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,6]
})

df.plot()
plt.show()