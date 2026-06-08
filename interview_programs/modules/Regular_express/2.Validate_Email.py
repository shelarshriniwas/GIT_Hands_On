'''
Program 2.Validate_Email.py

Input:

abc@gmail.com

Output:

Valid Email

'''

import re

email = input("Enter Email: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")