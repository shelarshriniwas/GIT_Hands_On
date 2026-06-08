#program_02_Time-series_slicing.py

import numpy as np

sales = np.array([
    100,120,150,180,200,
    250,300,350,400,450,
    500,550
])

print("Quarter 1")
print(sales[:3])

print("Quarter 2")
print(sales[3:6])