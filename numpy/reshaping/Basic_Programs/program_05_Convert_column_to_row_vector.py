#program_05_Convert_column_to_row_vector.py

import numpy as np

column = np.array([
    [10],
    [20],
    [30]
])

row = column.reshape(1,-1)

print(row)