# Check leap year.
import calendar

year = int(input("Enter Year : "))

if calendar.isleap(year):
    print("Leap Year")
else:
    print("Not Leap Year")