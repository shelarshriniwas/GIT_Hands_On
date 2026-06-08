#program_09_Plot_Series_data.py

import pandas as pd

s = pd.Series(
    [10,20,30,40,50]
)

s.plot()
plt.show()