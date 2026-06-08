# Count total files in folder.
import os

folder_path = input("Enter Folder Path : ")

count = 0

for item in os.listdir(folder_path):

    full_path = os.path.join(folder_path, item)

    if os.path.isfile(full_path):
        count += 1

print("Total Files :", count)