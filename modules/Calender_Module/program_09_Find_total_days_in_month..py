# Find total days in month.
import calendar

year = int(input("Enter Year : "))
month = int(input("Enter Month : "))

days = calendar.monthrange(year, month)[1]

print("Total Days :", days)