#program_10_Reshape_user_input_data.py

import numpy as np

data = list(map(int,input("Enter 6 numbers: ").split()))

arr = np.array(data)

result = arr.reshape(2,3)

print(result)