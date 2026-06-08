# program_06_Password_validation_system.py

import re

password = "Python@123"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).+$'

if re.match(pattern, password):
    print("Strong Password")

else:
    print("Weak Password")