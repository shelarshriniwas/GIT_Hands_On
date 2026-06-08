#program_04_Convert_dataset_into_batches.py

import numpy as np

data = np.arange(100)

batches = data.reshape(10,10)

print(batches)