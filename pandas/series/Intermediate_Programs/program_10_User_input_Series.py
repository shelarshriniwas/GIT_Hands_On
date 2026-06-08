#program_10_User_input_Series.py

import pandas as pd

n = int(input("Enter number of elements: "))

data = []

for i in range(n):
    value = int(input("Enter value: "))
    data.append(value)

s = pd.Series(data)

print(s)