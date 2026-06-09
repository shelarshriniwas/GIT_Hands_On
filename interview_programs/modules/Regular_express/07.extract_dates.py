
import re

text = "Today is 08-06-2026 and meeting is on 15-07-2026"

dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)

print(dates)