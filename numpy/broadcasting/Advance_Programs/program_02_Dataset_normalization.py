#program_02_Dataset_normalization.py

import numpy as np

data = np.array([
    [100,20],
    [200,40],
    [300,60]
])

normalized = (
    data - data.mean(axis=0)
) / data.std(axis=0)

print(normalized)