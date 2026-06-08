'''
Input:

Contact us at abc@gmail.com and xyz@yahoo.com

Output:

['abc@gmail.com', 'xyz@yahoo.com']
'''

import re

text = "Contact us at abc@gmail.com and xyz@yahoo.com"

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

print(emails)