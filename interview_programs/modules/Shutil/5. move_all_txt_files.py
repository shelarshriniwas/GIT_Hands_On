import os
import shutil

source = "Source Folder"
destination = "Destination Folder"

for file in os.listdir(source):

    if file.endswith(".txt"):
        shutil.move(
            os.path.join(source, file),
            os.path.join(destination, file)
        )

print("All .txt files moved")