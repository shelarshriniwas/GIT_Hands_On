#program_10_Performance_optimization.py

import numpy as np
import time

data = np.random.rand(
    1000000
)

start = time.time()

result = data + 10

end = time.time()

print(
    "Time:",
    end - start
)