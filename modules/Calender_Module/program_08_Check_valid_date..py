# Check valid date.
import calendar

year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
day = int(input("Enter Day : "))

valid = calendar.monthrange(year, month)[1]

if day <= valid:
    print("Valid Date")
else:
    print("Invalid Date")