#program_02_Tensor_reshaping.py

import numpy as np

tensor = np.arange(48)

tensor = tensor.reshape(
    2,
    3,
    4,
    2
)

print(tensor.shape)