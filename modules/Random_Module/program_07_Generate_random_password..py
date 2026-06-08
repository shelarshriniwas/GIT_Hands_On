# Generate random password.


import random
import string

characters = string.ascii_letters + string.digits

password = ""

for i in range(8):

    password += random.choice(characters)

print("Password :", password)