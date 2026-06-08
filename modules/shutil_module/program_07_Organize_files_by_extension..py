import os
import shutil

folder = "downloads"

for file in os.listdir(folder):
    ext = file.split(".")[-1]
    new_folder = f"{folder}/{ext}"

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    shutil.move(f"{folder}/{file}", f"{new_folder}/{file}")

print("Organized")