#program_10_Performance_comparison_of_slicing.py

import numpy as np
import time

arr = np.arange(10000000)

start = time.time()

slice_arr = arr[1000:9000000]

end = time.time()

print("Time Taken:", end-start)