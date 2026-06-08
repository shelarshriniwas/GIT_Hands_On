#program_04_Convert_row_to_column_vector.py

import numpy as np

row = np.array([10,20,30,40])

column = row.reshape(-1,1)

print(column)