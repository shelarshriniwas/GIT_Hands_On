#program_10_Deep_learning_dataset_preparation.py

import numpy as np

samples = 1000
features = 20

data = np.random.rand(
    samples,
    features
)

batch_size = 100

dataset = data.reshape(
    10,
    batch_size,
    features
)

print(dataset.shape)