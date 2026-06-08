import os

folder = os.getcwd()

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path) and os.path.getsize(path) == 0:
        print(file)