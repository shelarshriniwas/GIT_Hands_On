# program_05_Validate_email_format.py

import re

email = "test@gmail.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")

else:
    print("Invalid Email")


email = "test@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")

else:
    print("Invalid Email")