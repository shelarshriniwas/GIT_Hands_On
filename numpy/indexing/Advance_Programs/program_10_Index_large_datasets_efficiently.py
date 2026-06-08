#program_10_Index_large_datasets_efficiently.py

import numpy as np

data = np.random.randint(
    1,
    1000,
    1000000
)

result = data[data > 900]

print(result[:20])
print("Count:", len(result))