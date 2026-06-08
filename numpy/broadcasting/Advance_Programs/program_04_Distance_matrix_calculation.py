#program_04_Distance_matrix_calculation.py

import numpy as np

points = np.array([
    [1,2],
    [3,4],
    [5,6]
])

distance = points[:,None,:] - points

print(distance)