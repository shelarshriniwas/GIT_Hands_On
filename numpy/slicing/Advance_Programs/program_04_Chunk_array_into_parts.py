#program_04_Chunk_array_into_parts.py

import numpy as np

arr = np.arange(1,21)

chunks = np.array_split(arr,4)

for chunk in chunks:
    print(chunk)