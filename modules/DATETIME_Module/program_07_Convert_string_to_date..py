# Convert string to date.

from datetime import datetime

date_string = "28-05-2026"

converted_date = datetime.strptime(date_string, "%d-%m-%Y")

print(converted_date)