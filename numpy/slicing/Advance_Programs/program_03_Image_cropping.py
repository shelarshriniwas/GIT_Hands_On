#program_03_Image_cropping.py

import numpy as np

image = np.random.randint(
    0,
    255,
    (100,100)
)

cropped = image[20:80,20:80]

print(cropped.shape)