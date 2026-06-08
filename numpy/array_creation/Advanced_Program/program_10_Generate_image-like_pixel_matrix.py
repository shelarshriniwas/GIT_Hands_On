# program_10_Generate_image-like_pixel_matrix.py

import numpy as np

image = np.random.randint(
    0,
    256,
    (256,256),
    dtype=np.uint8
)

print(image)