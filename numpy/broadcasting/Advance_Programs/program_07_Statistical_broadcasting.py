#program_07_Statistical_broadcasting.py

import numpy as np

data = np.array([
    [10,20,30],
    [40,50,60]
])

mean = data.mean(axis=0)

centered = data - mean

print(centered)