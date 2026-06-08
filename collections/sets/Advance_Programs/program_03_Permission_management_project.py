# program_03_Permission_management_project.py

permissions = {"read", "write", "delete"}

check_permission = "write"

if check_permission in permissions:
    print("Permission Granted")
else:
    print("Permission Denied")

permissions.add("delete")

print(permissions)