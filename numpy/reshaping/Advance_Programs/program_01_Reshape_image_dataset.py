#program_01_Reshape_image_dataset.py

import numpy as np

images = np.random.randint(
    0,
    255,
    (100,784)
)

reshaped = images.reshape(
    100,
    28,
    28
)

print(reshaped.shape)