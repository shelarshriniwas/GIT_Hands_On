#program_05_Calculate_percentage_values.py

import numpy as np

sales = np.array([100,200,300])

total = sales.sum()

percentage = (sales / total) * 100

print(percentage)