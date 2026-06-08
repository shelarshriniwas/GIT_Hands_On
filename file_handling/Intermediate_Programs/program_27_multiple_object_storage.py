# program_27_multiple_object_storage.py

import pickle

data = [
    {"id": 101, "name": "Shri"},
    {"id": 102, "name": "Ram"}
]

with open("multiple.pkl", "wb") as file:

    pickle.dump(data, file)

print("Multiple Objects Stored")