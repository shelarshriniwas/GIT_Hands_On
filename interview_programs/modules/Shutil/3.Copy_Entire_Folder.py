'''
Input:

Source Folder
Destination Folder

Output:

Folder Copied Successfully
'''

import shutil
import os

source = "source_folder"
destination = "destination_folder"

os.makedirs(destination, exist_ok=True)

shutil.copytree(
    source,
    os.path.join(destination, "backup"),
    dirs_exist_ok=True
)

print("Folder Copied Successfully")