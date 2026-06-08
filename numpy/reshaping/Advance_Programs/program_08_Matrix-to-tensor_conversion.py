#program_08_Matrix-to-tensor_conversion.py

import numpy as np

matrix = np.arange(24).reshape(6,4)

tensor = matrix.reshape(
    2,
    3,
    4
)

print(tensor.shape)