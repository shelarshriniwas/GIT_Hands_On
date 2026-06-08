import re

mobile = "9876543210"

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")