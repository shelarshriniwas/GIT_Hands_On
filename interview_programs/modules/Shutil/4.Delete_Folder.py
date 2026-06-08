'''

Input:

TestFolder

Output:

Folder Deleted
'''

import shutil

folder = "TestFolder"

shutil.rmtree(folder)

print("Folder Deleted")