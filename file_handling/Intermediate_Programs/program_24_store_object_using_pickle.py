# program_24_store_object_using_pickle.py

import pickle

student = {
    "name": "Shri",
    "marks": 90
}

with open("student.pkl", "wb") as file:

    pickle.dump(student, file)

print("Object Stored")