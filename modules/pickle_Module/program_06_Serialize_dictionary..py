import pickle

data = {"a": 1, "b": 2}

with open("dict.pkl", "wb") as f:
    pickle.dump(data, f)

print("Dictionary saved")