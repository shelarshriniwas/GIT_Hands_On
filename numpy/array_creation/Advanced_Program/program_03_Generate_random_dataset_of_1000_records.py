# program_03_Generate_random_dataset_of_1000_records.py

import numpy as np

data = np.random.randint(1,100,(1000,5))

print(data.shape)
print(data)