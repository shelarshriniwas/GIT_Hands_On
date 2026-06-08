import os

folder = "files"

for i, file in enumerate(os.listdir(folder)):
    new_name = f"file_{i}.txt"
    os.rename(f"{folder}/{file}", f"{folder}/{new_name}")

print("Renamed")