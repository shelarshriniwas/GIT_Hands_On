# Count Sundays in month.
import calendar

year = int(input("Enter Year : "))
month = int(input("Enter Month : "))

count = 0

month_data = calendar.monthcalendar(year, month)

for week in month_data:

    if week[calendar.SUNDAY] != 0:
        count += 1

print("Total Sundays :", count)