import os

folder = os.getcwd()

count = 0

for root, dirs, files in os.walk(folder):
    count += len(files)

print("Total Files =", count)