'''
Input
ProjectFolder
Output
ProjectFolder_2026-06-09
'''

import shutil
from datetime import datetime

source = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation_Script\\Automation Files"

date = datetime.now().strftime("%Y-%m-%d")

destination = f"{source}_{date}"

shutil.copytree(source, destination)

print("Backup Created")