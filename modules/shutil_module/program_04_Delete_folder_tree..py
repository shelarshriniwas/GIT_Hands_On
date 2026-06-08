import shutil
import os

folder = "temp_folder"

if os.path.exists(folder):
    shutil.rmtree(folder)
    print("Deleted")
else:
    print("Folder not found")