# program_25_load_pickle_object.py

import pickle

with open("student.pkl", "rb") as file:

    data = pickle.load(file)

print(data)