#program_04_Apply_function_on_Series.py

import pandas as pd

s = pd.Series([1,2,3,4,5])

result = s.apply(lambda x: x*x)

print(result)