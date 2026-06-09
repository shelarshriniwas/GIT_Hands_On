

import re

text = "Learning #Python and #Automation"

hashtags = re.findall(r'#\w+', text)

print(hashtags)