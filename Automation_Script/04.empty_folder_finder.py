import os

path = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation_Script\\Automation Files"

for folder in os.listdir(path):
    folder_path = os.path.join(path, folder)

    if os.path.isdir(folder_path):
        if not os.listdir(folder_path):
            print(folder)