# program_36_backup_file_system.py
source = input("Enter Source File : ")
backup = input("Enter Backup File : ")

with open(source, "r") as file:
    data = file.read()

with open(backup, "w") as file:
    file.write(data)

print("Backup Created")

# Restore 

backup = input("Enter Backup File : ")
restore = input("Enter Restore File : ")

with open(backup, "r") as file:
    data = file.read()

with open(restore, "w") as file:
    file.write(data)

print("Backup Restored")