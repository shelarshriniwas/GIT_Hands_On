import os
import shutil

src = "A"
dst = "B"

for file in os.listdir(src):
    if file not in os.listdir(dst):
        shutil.copy(f"{src}/{file}", f"{dst}/{file}")

print("Synced")