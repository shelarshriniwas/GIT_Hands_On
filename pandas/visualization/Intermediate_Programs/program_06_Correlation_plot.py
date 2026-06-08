#program_06_Correlation_plot.py

import pandas as pd

df = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})

corr = df.corr()

print(corr)