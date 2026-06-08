#program_03_Feature_scaling.py

import numpy as np

data = np.array([
    [10],
    [20],
    [30],
    [40]
])

scaled = (
    data - data.min()
) / (
    data.max() - data.min()
)

print(scaled)