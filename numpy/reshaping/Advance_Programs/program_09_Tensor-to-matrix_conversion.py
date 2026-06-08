#program_09_Tensor-to-matrix_conversion.py

import numpy as np

tensor = np.arange(24).reshape(
    2,
    3,
    4
)

matrix = tensor.reshape(6,4)

print(matrix)