#program_07_Concatenate_DataFrames.py
import pandas as pd

df1 = pd.DataFrame({"A":[1,2]})
df2 = pd.DataFrame({"A":[3,4]})

result = pd.concat([df1,df2])

print(result)