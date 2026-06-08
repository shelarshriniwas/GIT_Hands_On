# Print weekday name.

from datetime import datetime

today = datetime.now()

weekday = today.strftime("%A")

print("Weekday :", weekday)