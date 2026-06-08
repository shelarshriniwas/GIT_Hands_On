import re

pan = "ABCDE1234F"

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"

if re.match(pattern, pan):
    print("Valid PAN")
else:
    print("Invalid PAN")