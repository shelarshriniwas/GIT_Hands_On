import os

folder = "data"

for file in os.listdir(folder):
    path = f"{folder}/{file}"

    if os.path.getsize(path) == 0:
        os.remove(path)

print("Cleaned empty files")