import pickle

data = [10, 20, 30]

with open("list.pkl", "wb") as f:
    pickle.dump(data, f)

print("List saved")