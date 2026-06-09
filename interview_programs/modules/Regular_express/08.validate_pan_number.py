
import re

pan = "ABCDE1234F"

if re.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]', pan):
    print("Valid PAN")
else:
    print("Invalid PAN")