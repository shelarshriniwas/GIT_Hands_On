import pickle

class Demo:
    def __init__(self):
        self.value = 100

obj = Demo()

with open("obj.pkl", "wb") as f:
    pickle.dump(obj, f)

print("Object saved")