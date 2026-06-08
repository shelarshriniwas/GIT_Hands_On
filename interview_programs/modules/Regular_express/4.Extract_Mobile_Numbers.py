'''
Input:

Call 9876543210 or 9123456789

Output:

['9876543210', '9123456789'] 
'''

import re

text = "Call 9876543210 or 9123456789"

numbers = re.findall(r'\d{10}', text)

print(numbers)