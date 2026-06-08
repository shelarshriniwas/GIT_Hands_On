# Format date using strftime().

from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y")

print(formatted_date)