'''
Input:

Source Folder
Backup Folder

Output:

Backup Completed
'''

import shutil
from datetime import datetime
import os

source_folder = "SourceFolder"
backup_folder = "BackupFolder"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

destination = os.path.join(
    backup_folder,
    f"backup_{timestamp}"
)

shutil.copytree(source_folder, destination)

print("Backup Completed")