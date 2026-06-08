import shutil
import datetime

time = datetime.datetime.now().strftime("%Y%m%d%H%M")

shutil.copytree("project", f"project_backup_{time}")

print("Timestamp backup created")