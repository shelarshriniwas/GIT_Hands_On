'''
Input:

Length = 8

Output:

A7x@9PqL

'''

import random
import string

length = 8

chars = string.ascii_letters + string.digits + "@#$%&*"

password = ''.join(random.choices(chars, k=length))

print(password)