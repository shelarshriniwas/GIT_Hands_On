import os
from pathlib import Path

path = "C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation"

print(path)

print(os.chdir("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation"))


print(os.getcwd())

os.makedirs("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation\\Practice-1\\Practice-2\\Practice-3")

os.rmdir("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation\\Practice-3")

os.remove("osfile.txt")

os.rename("osfile.txt", "osfile_new.txt")

s = os.path.exists("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation")

print(s)

d = os.path.join("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects","Automation")

print(d)


s1 = Path.is_dir("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation")

print(s1)

s2 = Path.is_file("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation")

print(s2)

s3 = Path.iterdir("C:\\Users\\Shriniwas\\VS_Codes\\Python_Projects\\Automation")

print(s3)
