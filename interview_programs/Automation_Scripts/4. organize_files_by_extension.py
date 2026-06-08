import os
import shutil

folder = "Downloads"

for file in os.listdir(folder):

    source = os.path.join(folder, file)

    if os.path.isfile(source):

        ext = os.path.splitext(file)[1][1:].upper()

        if ext:

            destination = os.path.join(folder, ext)

            os.makedirs(destination,
                        exist_ok=True)

            shutil.move(
                source,
                os.path.join(destination, file)
            )

print("Files Organized Successfully")