#program_08_Feature_engineering.py

import pandas as pd

sales = pd.Series([100,200,300,400])

growth = sales.pct_change()

print(growth)