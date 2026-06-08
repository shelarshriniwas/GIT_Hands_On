#program_06_Statistical_analysis.py

import pandas as pd

s = pd.Series([10,20,30,40,50])

print("Mean =", s.mean())
print("Median =", s.median())
print("Std =", s.std())
print("Variance =", s.var())