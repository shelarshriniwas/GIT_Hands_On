import pickle

data = {"name": "Rahul", "age": 25}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

print("Object Stored")
 

with open("data.pkl", "rb") as f:
    obj = pickle.load(f)

print(obj)