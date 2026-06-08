import pickle

employee = {"id": 101, "name": "Amit", "salary": 50000}

with open("emp.pkl", "wb") as f:
    pickle.dump(employee, f)

print("Employee saved")