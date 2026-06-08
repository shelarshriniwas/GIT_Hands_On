import pickle

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Amit"}
]

with open("students.pkl", "wb") as f:
    pickle.dump(students, f)

print("Saved")