import re

password = "Pass@123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).{8,}$"

if re.match(pattern, password):
    print("Strong")
else:
    print("Weak")