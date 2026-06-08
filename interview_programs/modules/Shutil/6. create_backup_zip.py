import shutil

shutil.make_archive(
    "project_backup",
    "zip",
    "Project Folder"
)

print("project_backup.zip")