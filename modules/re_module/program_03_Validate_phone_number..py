import re

phone = "9876543210"

pattern = r"^\d{10}$"

if re.match(pattern, phone):
    print("Valid")
else:
    print("Invalid")