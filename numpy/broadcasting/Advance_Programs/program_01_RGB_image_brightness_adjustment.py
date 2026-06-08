#program_01_RGB_image_brightness_adjustment.py

import numpy as np

image = np.random.randint(
    0,
    255,
    (100,100,3)
)

bright_image = image + 50

print(bright_image.shape)