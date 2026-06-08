import pickle

inventory = {"Laptop": 10, "Mouse": 50}

with open("inventory.pkl", "wb") as f:
    pickle.dump(inventory, f)

print("Saved")