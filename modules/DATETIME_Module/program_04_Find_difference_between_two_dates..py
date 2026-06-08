# Find difference between two dates.

from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 5, 28)

difference = date2 - date1

print("Difference :", difference.days, "days")
