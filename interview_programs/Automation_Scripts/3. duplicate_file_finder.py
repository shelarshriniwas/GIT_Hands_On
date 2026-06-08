import os
import hashlib

folder = "test_folder"

hashes = {}

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    if os.path.isfile(path):

        with open(path, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if file_hash in hashes:
            print("Duplicate:", file)
        else:
            hashes[file_hash] = file