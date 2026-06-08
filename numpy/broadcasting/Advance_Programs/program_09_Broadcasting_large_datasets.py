#program_09_Broadcasting_large_datasets.py

import numpy as np

data = np.random.rand(
    100000,
    10
)

result = data + 5

print(result.shape)