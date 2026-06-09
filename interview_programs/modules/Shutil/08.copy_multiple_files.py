

import shutil

files = ["file1.txt", "file2.txt"]

for file in files:
    shutil.copy2(file, "Backup")

print("Files copied successfully")