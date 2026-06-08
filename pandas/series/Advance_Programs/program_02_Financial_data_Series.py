#program_02_Financial_data_Series.py

import pandas as pd

stocks = pd.Series(
    [150,155,160,158,165],
    index=["Mon","Tue","Wed","Thu","Fri"]
)

print(stocks)