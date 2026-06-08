#program_08_Neural_network_computations.py

import numpy as np

inputs = np.array([
    [1,2],
    [3,4]
])

weights = np.array([
    [0.5,0.2],
    [0.3,0.8]
])

bias = np.array([1,1])

output = np.dot(inputs,weights) + bias

print(output)