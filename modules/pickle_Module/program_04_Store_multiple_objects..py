import pickle

data = [1, 2, 3, "Python"]

with open("multi.pkl", "wb") as f:
    pickle.dump(data, f)

print("Stored")